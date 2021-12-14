from decimal import Decimal 
from pprint import pprint 
from typing import List
from qbodbc.utils import Ref
from qbodbc.objects.base_object import BaseObject 

class BillItemLine(BaseObject): 
    """
    Add a line item to a bill. Minimum required fields. Other items: 
        - class: ItemLineClassRefFullName
        - customer: ItemLineCustomerRefFullName
        - customer:job: ItemLineCustomerRefFullName
        - cogs account: ItemLineOverrideItemAccountRefFullName  
    """
    __table_name__ = 'BillItemLine'

    def __init__(self, Item: str, Desc: str, Quantity: Decimal, Amount: Decimal, **kwargs): 
        self.ItemLineItemRefFullName = Item
        self.ItemLineDesc = Desc
        self.ItemLineQuantity = Quantity
        self.ItemLineCost = Amount
        self.FQSaveToCache = 1 # Default to save 
        # Overide defaults 
        self.ItemLineItemRefListId = kwargs.pop('ItemLineItemRefListId', None)
        self.ItemLineCustomerRefFullName = kwargs.pop('ItemLineCustomerRefFullName', None)
        self.ItemLineOverrideItemAccountRefFullName = kwargs.pop('ItemLineOverrideItemAccountRefFullName', None)
        self.ItemLineClassRefFullName = kwargs.pop('ItemLineClassRefFullName', None)

    def __repr__(self):
        [(x['ItemRefFullName'], x['ItemLineQuantity'],) for x in self] 
        return ''
        
class BillExpenseLine(BaseObject):
    __table_name__ = 'BillExpenseLine'

    def __init__(self, account: str, memo: str, amount: Decimal, **kwargs): 
        self.ExpenseLineAccountRefFullName = account
        self.ExpenseLineMemo = memo
        self.ExpenseLineAmount = amount
 

class Bill(BaseObject):
    __table_name__ = 'Bill'

    def __init__(self, **kwargs): 
        """Bill with minimum field requirements.""" 
        self.VendorRefFullName = kwargs.pop('VendorRefFullName', None)
        self.APAccountRefFullName = kwargs.pop('APAccountRefFullName', None)
        self.TxnDate = kwargs.pop('TxnDate', None)
        self.RefNumber = kwargs.pop('RefNumber', None)
        self.Memo = kwargs.pop('Memo', None)
        # [setattr(self, k, v) for k,v in kwargs.items()]
        
        # List of dictionaries 
        self._line_item = [] 
        # self.BillLineItems = BillItemLine() 
        self._line_expense = [] 
        # self.BillLineExpense = BillExpenseLine() 

    def add_item(self, item):
        """
        Take BillLineItem objects: list or single object
        """
        if isinstance(item, list): 
            [self._line_item.append(i) for i in item]
        else: 
            self._line_item.append(item)

    def add_expense(self, expense): 
        """Add an expense item to a bill."""
        if isinstance(expense, list): 
            [self._line_expense.append(i) for i in expense]
        else: 
            self._line_expense.append(expense)

    def save(self, qb=''):
        """        
        If an item, and expense are required, the bill must exist before 
        the new insert can be preformed. 

        Overide the default method since it needs to work on an iterable. 

        Pop an item in the list and assign the current bill args to it. 
        """
        try: 
            while self._line_item: 
                print('***', len(self._line_item), '***')

                head = self._line_item.pop(0)
                head.update_obj(self)

                if len(self._line_item) == 0:    
                    # Update FQSaveToCache == 0 
                    head.FQSaveToCache = 0
                    qb.cursor.execute(head.create(), head.to_values())
                else: 
                    qb.cursor.execute(head.create(), head.to_values())

            return {
                'Vendor': self.VendorRefFullName, 
                'RefNum': self.RefNumber,
                # Last insert on a parent table will still refrence an insert on the child table
                "id": qb.last_insert(self.__table_name__)
                }

        except Exception as e:
            return {
                "id": e.args[-1],
                "key": self.RefNumber
            }
       
       
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
            Line Items: {len(self._line_item)} Expense Items: {len(self._line_expense)}
            """
