import pytest 
from qbodbc.utils import process_insert, as_decimal, as_date
from qbodbc.objects import Bill
from qbodbc import QB 

bill_test = Bill(vendor = "Computer Store", 
        account = "Accounts Payable", 
        date = as_date(2020, 1, 1), 
        ref_num = "12331-1231", 
        memo = "PO123312", 
        DueDate = as_date(2021,1,1)
        )

bill_test.add_item(item='Books for Resale',
        memo= "OverRideTheDefault",
        quantity = as_decimal(2),
        amount = as_decimal(10.99)
        )

bill_test.add_expense(account = "Utilities",
        memo= "testMemo",
        amount = as_decimal(10.99)
        )

# Connect using a QB object to enforce UTF-8 encoding
con = QB("qbtest")

def test_exists(): 
        bill_test

def test_bill(): 
    assert bill_test.header["VendorRefFullName"] == "Computer Store"

def test_add(): 
    assert bill_test.line_item[0]["ItemLineItemRefFullName"] == "Books for Resale"
    assert bill_test.line_expense[0]["ExpenseLineMemo"] == "testMemo"



def test_bill_inserts(): 
        # # Test the inserts 
        bill_header = process_insert(bill_test.header, "Bill")
        assert bill_header == "INSERT INTO Bill (VendorRefFullName, APAccountRefFullName, TxnDate, RefNumber, Memo, DueDate) VALUES (?,?,?,?,?,?)"

        bill_item_line = process_insert(bill_test.line_item[0], "BillItemLine")
        assert bill_item_line == "INSERT INTO BillItemLine (ItemLineItemRefFullName, ItemLineDesc, ItemLineQuantity, ItemLineCost) VALUES (?,?,?,?)"
        
        bill_expense_line = process_insert(bill_test.line_expense[0], "BillExpenseLine")
        assert bill_expense_line == "INSERT INTO BillExpenseLine (ExpenseLineAccountRefFullName, ExpenseLineMemo, ExpenseLineAmount) VALUES (?,?,?)"


def test_bill_add(): 
        # Final implementation 
        resp = con.create(bill_test)
        assert resp["vendor"] == bill_test.header["VendorRefFullName"]

def test_close_connection(): 
        con.close()


# con.query("SELECT * FROM Bill")

# # Cache results 
# Bill.get_args(con)
# assert list(Bill.args["COLUMNNAME"]) == list(bill_test.args["COLUMNNAME"])

# Bill.get_table(con)
# assert list(Bill._table["TxnID"]) == list(bill_test._table["TxnID"])
