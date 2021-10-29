from qbodbc import QB
from qbodbc.objects import Bill 
from qbodbc.utils import as_decimal

import datetime         
from decimal import Decimal

# Create a bill 
test_bill = Bill(vendor = "Data Storage Co.", 
    date = datetime.date(2021, 1, 1), 
    account= "Accounts Payable",
    memo = "POSuperMemo", 
    ref_num = "ItemExpenseTest", 
    DueDate = datetime.date(2021,1,30)
    )

# Add a line item 
test_bill.add_item(
    "Deposit", "Deposit for future work.", as_decimal(1), 
    as_decimal(99.99) 
    # ItemLineClassRefFullName = "Project"
    )

# Add an expense line 
test_bill.add_expense(
    account="Utilities", 
    memo="Add an expense line", 
    amount = as_decimal(100)
)

# Open a connection with QuickBooks
con = QB("qbtest")

# Inspect the bill 
test_bill


# Create the bill using the connection object
bill_resp = con.create(test_bill)

# Close the connection 
con.close()

