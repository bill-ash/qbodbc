import qbodbc
from qbodbc.bill import Bill 
from qbodbc.utils import format_decimal, process_insert
import datetime         
from qbodbc import QB
from decimal import Decimal

## Insert a bill using raw sql 

import pyodbc
import pandas as pd 

con = pyodbc.connect("DSN=qbtest")
cx = con.cursor()

bill_line = pd.read_sql("SELECT * FROM BillExpenseLine", con)
bill_line.head()
bill_line.columns

bill_header = pd.read_sql("SELECT * FROM Bill", con)
bill_header.head()
bill_header.columns

expense_account = pd.read_sql("SELECT * FROM Account", con)
expense_account.head()
expense_account.columns
[i for i in expense_account["FullName"]]

vendors = pd.read_sql("SELECT * FROM Vendor", con)
vendors.head()
vendors.columns
[i for i in vendors["Name"]]


bill_line_insert = {
    "ExpenseLineAccountRefFullName": "Utilities", 
    "ExpenseLineAmount": 23.99, 
    "ExpenseLineMemo" : "testbillone", 
    "FQSaveToCache": 1
}

bill_header_insert = {
    "VendorRefFullName": "Forward Travel", 
    "APAccountRefFullName": "Accounts Payable", 
    "TxnDate": datetime.date(2021, 8, 25), 
    "RefNumber": "t123321", 
    "DueDate": datetime.date(2021, 9, 1),
    "Memo": "TEST INSERT PO 123321" 
}

qb_con = QB("qbtest")

process_insert(bill_line_insert, "BillExpenseLine")
process_insert(bill_header_insert, "Bill")


format_decimal(bill_header_insert.values())
format_decimal(bill_line_insert.values())
# Paramterized queries and date times work 
zz = ['Utilities'.encode("utf-8"), Decimal("23.11"), 'testerone'.encode("utf-8"), Decimal(1)]
cx.execute(process_insert(bill_line_insert, "BillExpenseLine"), *zz)
# cx.execute(process_insert(bill_line_insert, "BillExpenseLine"), 'Utilities'.encode("utf-8"), Decimal(23.99), 'testerone'.encode("utf-8"), Decimal(1))
cx.execute(
    """
    INSERT INTO Bill    
        (VendorRefFullName, APAccountRefFullName, TxnDate, RefNumber, DueDate, Memo) 
    VALUES (?, ?, ?, ?, ?, ?)
    """, 
    (
        "Forward Travel".encode("utf-8"), "Accounts Payable".encode("utf-8"), datetime.date(2021,8,25),
        "23131212".encode("utf-8"), datetime.date(2021,9,25), "testinserPO231231".encode("utf-8")
    )
)

# Raw SQL 
cx.execute("INSERT INTO BillExpenseLine (ExpenseLineAccountRefFullName, ExpenseLineAmount, ExpenseLineMemo, FQSaveToCache) VALUES ('Utilities', 23.99, 'testbillone', 1)")
cx.execute("INSERT INTO Bill (VendorRefFullName, APAccountRefFullName, TxnDate, RefNumber, DueDate, Memo) VALUES ('Forward Travel', 'Accounts Payable', {d'2021-08-25'}, 't4212312', {d'2021-09-01'}, 'TEST INSERT PO 123321')")

cx.execute("sp_lastinsertid bill").fetchone()
cx.execute("sp_lastinsertid BillExpenseLine").fetchone()

cx.close()

# Test Bill 

test_bill = Bill(
    date = datetime.date(2020, 1, 1), 
    memo = "SomeMemo", 
    ref_num = "123321", 
    bill_class = "Project"
    )

test_bill.header

names = list(test_bill.header.keys())
vals = list(test_bill.header.values())

