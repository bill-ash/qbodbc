from dataclasses import dataclass
from qbodbc import QB 
from qbodbc.utils import * 
import pandas as pd 

# @dataclass
# class Bill: 
#     TxnDate: str
#     RefNum: str
#     Memo: str


class Bill: 
    # def __init__(self, date=None, ref_num=None, memo=None, bill_class=None): 
    def __init__(self, **kwargs): 
        # self.date = date
        # self.ref_num = ref_num 
        # self.memo = memo 
        # self.bill_class = bill_class
        self.header = {}
        self.line_item = [] 
        self.line_expense = [] 

    @staticmethod
    def get_args(con): 
        try: 
            bill_args = con.query("sp_columns Bill")
            return bill_args[bill_args["IS_NULLABLE"] == "YES"][["COLUMNNAME", "TYPENAME"]]
        except Exception as e: 
            print("Error: ", e)

    # @staticmethod
    # def get_args(con): 
    #     try: 
    #         bill_args = con.query("sp_columns Bill")
    #         return bill_args[bill_args["IS_NULLABLE"] == "YES"][["COLUMNNAME", "TYPENAME"]]
    #     except Exception as e: 
    #         print("Error: ", e)

    def add_item(self, data = []): 
        self.line_item.append(data)

    def add_expense(self, data = []): 
        self.line_expense.append(data)

    def _create(self, conn):
        # Add the bill line 
        # Add the bill header
        # Add the expense line 

        # for i in self.line_expense: 
        _line = process_insert(self.line_expense, "ExpenseBillLine")
        conn._connection.execute(
            """
            
            """
        )
        


    def __repr__(self):
        return f"""Bill: {self.header["ref_num"]}
        Line Items: {len(self.line_item)} Expense Items: {len(self.line_expense)}
        """ 
