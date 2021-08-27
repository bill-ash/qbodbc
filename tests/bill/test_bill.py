import pytest 
from qbodbc.utils import process_insert, as_decimal, as_date
from qbodbc.bill import Bill
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

def test_bill(): 
    assert bill_test.header["VendorRefFullName"] == "Computer Store"

def test_add(): 

    assert bill_test.line_item[0]["item"] == "Books for Resale"
    assert bill_test.line_expense[0]["memo"] == "OverRideTheDefault"


# # Connect using a QB object to enforce UTF-8 encoding
# con = QB("qbtest")
# bill_test


# # Update at insert with some logic 
# bill_test.line_expense[0]["FQSaveToCache"] = as_decimal(1)
# bill_test.line_item[0]["FQSaveToCache"] = as_decimal(1)

# # Test the inserts 
# bill_header = process_insert(bill_test.header, "Bill")
# bill_item_line = process_insert(bill_test.line_item[0], "BillItemLine")
# bill_expense_line = process_insert(bill_test.line_expense[0], "BillExpenseLine")

# # Insert item line 
# con._connection.execute(bill_item_line, *list(bill_test.line_item[0].values()))

# # Insert expense line 
# con._connection.execute(bill_expense_line, *list(bill_test.line_expense[0].values()))

# # Insert bill header 
# con._connection.execute(bill_header, *list(bill_test.header.values()))

# # Final implementation 
# # con.create(bill_test)

# con.query("SELECT * FROM Bill")

# # Cache results 
# Bill.get_args(con)
# assert list(Bill.args["COLUMNNAME"]) == list(bill_test.args["COLUMNNAME"])

# Bill.get_table(con)
# assert list(Bill._table["TxnID"]) == list(bill_test._table["TxnID"])

# con.close()