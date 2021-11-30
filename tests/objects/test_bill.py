from datetime import date 
from decimal import Decimal
import pytest 
from qbodbc.objects import Bill
from qbodbc import QuickBooks
from qbodbc.objects.bill import BillItemLine 
from tests.test_base import TestConf


session = QuickBooks(TestConf.DSN)
session.connect()
session.tables()

# bill_line_item = session.query('Select * from BillItemLine')

items = session.sql('select * from Item').fetchall()
vendor = session.sql('select * from vendor').fetchall()

ServiceItems = [c.FullName for c in items if c.Type == 'ItemService']

line_1 = BillItemLine(Item=ServiceItems[2], Desc='ItemServiceDescription', Quantity=2,
    Amount=Decimal('20.21'))

bill_test = Bill(Vendor = "Computer Store", APAccount = "Accounts Payable", 
        Date = date(2020, 1, 1), RefNumber = "12331-1231", Memo = "PO123312", 
        TxnDate = date(2021,1,1)
        )

bill_test.add_item(line_1)

# bill_test.add_item(item='Books for Resale',
#         memo= "OverRideTheDefault",
#         quantity = as_decimal(2),
#         amount = as_decimal(10.99)
#         )

# bill_test.add_expense(account = "Utilities",
#         memo= "testMemo",
#         amount = as_decimal(10.99)
#         )



# def test_exists(): 
#         bill_test

# def test_bill(): 
#     assert bill_test.header["VendorRefFullName"] == "Computer Store"

# def test_add(): 
#     assert bill_test.line_item[0]["ItemLineItemRefFullName"] == "Books for Resale"
#     assert bill_test.line_expense[0]["ExpenseLineMemo"] == "testMemo"



# def test_bill_inserts(): 
#         # # Test the inserts 
#         bill_header = process_insert(bill_test.header, "Bill")
#         assert bill_header == "INSERT INTO Bill (VendorRefFullName, APAccountRefFullName, TxnDate, RefNumber, Memo, DueDate) VALUES (?,?,?,?,?,?)"

#         bill_item_line = process_insert(bill_test.line_item[0], "BillItemLine")
#         assert bill_item_line == "INSERT INTO BillItemLine (ItemLineItemRefFullName, ItemLineDesc, ItemLineQuantity, ItemLineCost) VALUES (?,?,?,?)"
        
#         bill_expense_line = process_insert(bill_test.line_expense[0], "BillExpenseLine")
#         assert bill_expense_line == "INSERT INTO BillExpenseLine (ExpenseLineAccountRefFullName, ExpenseLineMemo, ExpenseLineAmount) VALUES (?,?,?)"


def test_bill_add(): 
        # Final implementation 
        resp = bill_test.save(qb=session)
        assert resp["vendor"] == bill_test.header["VendorRefFullName"]

# def test_close_connection(): 
#         con.close()

