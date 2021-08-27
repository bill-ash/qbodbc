from typing import Optional, List

from dataclasses import dataclass
from qbodbc import QB 
from qbodbc.utils import * 
import pandas as pd 
from decimal import Decimal 
from pprint import pprint 

class Bill:
    """Bill container."""
    # Cache the most recent calls for all objects.
    _table = None 
    args = None

    def __init__(self, 
        vendor: str,
        account: str, 
        date: datetime.date, 
        ref_num: str,
        memo: str,
        **kwargs):
        """Bill with minimum field requirements.""" 
        self.header = {
            key : value for key, value in {
                "VendorRefFullName": vendor,
                "APAccountRefFullName": account, 
                "TxnDate": date, 
                "RefNumber": ref_num,
                "Memo": memo,
                **kwargs
                }.items() if value is not None 
            }
        # List of dictionaries 
        self.line_item = [] 
        self.line_expense = [] 

    @classmethod
    def get_args(cls, con): 
        try: 
            bill_args = con.query("sp_columns Bill")
            args = bill_args[bill_args["IS_NULLABLE"] == "YES"][["COLUMNNAME", "TYPENAME"]]
            pprint(args)
            cls.args = args
        except Exception as e: 
            print("Error: ", e)

    @classmethod 
    def get_table(cls, con):
        """Cache results if a read is done."""
        cls._table = con.query("SELECT * FROM Bill")


    def add_item(self,
        item: str,
        memo: Optional[str],
        quantity: Decimal, 
        amount: Decimal, 
        **kwargs
        ) -> List:
        """"Add a line item to a bill. Minimum required fields."""
        bill_line = {
            key : value for key, value in {
                "ItemLineItemRefFullName": item,
                "ItemLineDesc": memo, 
                "ItemLineQuantity": quantity, 
                "ItemLineCost": amount,
                **kwargs
                }.items() if value is not None 
            }
        self.line_item.append(bill_line)

    def add_expense(self, 
        account: str, 
        memo: str, 
        amount: Decimal, 
        **kwargs): 
        """Add an expense item to a bill."""
        bill_line = {
            key : value for key, value in {
                "ExpenseLineAccountRefFullName": account,
                "ExpenseLineMemo": memo,  
                "ExpenseLineAmount": amount,
                **kwargs, 
                }.items() if value is not None 
            }
        self.line_expense.append(bill_line)

    def _create(self, conn):
        """Push bill instance to QuickBooks.
        
        Starts by adding a bill or expense line, cache the 
        result with QODBC, then adding the header. 

        If an item, and expense are required, the bill must exist before 
        the new insert can be preformed. 
        """
        if len(self.line_item) > 0:
            for i in self.line_item:
                i["FQSaveToCache"] = as_decimal(1)
                _line = process_insert(i , "BillItemLine")
                conn.execute(_line, *i.values())
            
            conn.execute(
                process_insert(self.header, "Bill"), *list(self.header.values())
                )
            
            last_bill = conn.execute("sp_lastinsertid Bill").fetchall()[0][0]

            if len(self.line_expense) > 0:     
                for i in self.line_expense: 
                    expense = {"TxnID": last_bill, **i}
                    _line = process_insert(expense , "BillExpenseLine")
                    conn.execute(_line, *list(expense.values()))
            
            # Output
            return {
                "vendor": self.header["VendorRefFullName"], 
                "ref_num": self.header["RefNumber"],
                "id": last_bill
                }
       
        else: 
            for i in self.line_expense: 
                i["FQSaveToCache"] = as_decimal(1)
                _line = process_insert(i , "BillExpenseLine")
                conn.execute(_line, *i.values())
            
            conn.execute(
                process_insert(self.header, "Bill"), *list(self.header.values())
                )
            
            last_bill = conn.execute("sp_lastinsertid Bill").fetchall()[0][0]

            # Output
            return {
                "vendor": self.header["VendorRefFullName"], 
                "ref_num": self.header["RefNumber"],
                "id": last_bill
                }



    def __repr__(self):
        return f"""
        Bill: {self.header["VendorRefFullName"]} - {self.header["RefNumber"]}
        Line Items: {len(self.line_item)} Expense Items: {len(self.line_expense)}
        """ 
