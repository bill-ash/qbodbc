from decimal import Decimal 
from pprint import pprint 
from typing import List
from qbodbc.utils import Ref
from qbodbc.objects.base_object import BaseObject 

class BillItemLine: 
    """
    Add a line item to a bill. Minimum required fields. Other items: 
        - class: ItemLineClassRefFullName
        - customer: ItemLineCustomerRefFullName
        - customer:job: ItemLineCustomerRefFullName
        - cogs account: ItemLineOverrideItemAccountRefFullName  
    """
    def __init__(self, Item: str, Desc: str, Quantity: Decimal, Amount: Decimal, **kwargs): 
        self.ItemLineItemRefFullName = Item
        self.ItemLineDesc = Desc
        self.ItemLineQuantity = Quantity
        self.ItemLineCost = Amount
        self.FQSaveToCache = 1 # Default to save 
        self.ItemLineItemRefListId = kwargs.pop('ItemLineItemRefListId', None)
        self.ItemLineCustomerRefFullName = kwargs.pop('ItemLineCustomerRefFullName', None)
        self.ItemLineOverrideItemAccountRefFullName = kwargs.pop('ItemLineOverrideItemAccountRefFullName', None)
        self.ItemLineClassRefFullName = kwargs.pop('ItemLineClassRefFullName', None)

class BillExpenseLine:
    def __init__(self, account: str, memo: str, amount: Decimal, **kwargs): 
        self.ExpenseLineAccountRefFullName = account
        self.ExpenseLineMemo = memo
        self.ExpenseLineAmount = amount
 



class Bill(BaseObject):
    __table__name__ = 'BillItemLine'

    def __init__(self, **kwargs): 
        """Bill with minimum field requirements.""" 
        
        self.VendorRefFullName = kwargs.pop('Vendor', None)
        self.APAccountRefFullName = kwargs.pop('APAccount', None)
        self.TxnDate = kwargs.pop('TxnDate', None)
        self.RefNumber = kwargs.pop('RefNumber', None)
        self.Memo = kwargs.pop('Memo', None)
        
        # List of dictionaries 
        self.line_item = [] 
        self.line_expense = [] 

    def add_item(self, item):
        """
        Takes a list of dictionaries or a single dictionary
        """
        if isinstance(item, list): 
            [self.line_item.append(i) for i in item]
        else: 
            self.line_item.append(item)

    def add_expense(self, expense): 
        ...
        # """Add an expense item to a bill."""
        # bill_line = {
        #     key : value for key, value in {
        #         }.items() if value is not None 
        #     }
        # self.line_expense.append(bill_line)

    def create(self, conn):
        """
        Push bill instance to QuickBooks.
                
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
    
    def save(self, qb): 
        
        for i in self.line_item: 
            

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


    def __repr__(self):
        return f"""
            Bill: {self.VendorRefFullName}: {self.RefNumber}
            Line Items: {len(self.line_item)} Expense Items: {len(self.line_expense)}
            """
