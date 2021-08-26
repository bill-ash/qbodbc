from qbodbc.bill import Bill
import datetime


bill_test = Bill(
    date = datetime.date(2020, 1, 1),
    ref_num = "test-num", 
    memo = "PO123", 
    bill_class = "class"
    )


bill_test.add_item(['itemid', 2, 10.99, 'ProjClass', 'Customer1'])
bill_test.add_item(['itemid1', 1, 20.99, 'ProjClass', 'Customer1'])
bill_test.add_item(['itemid2', 4, 2.01, 'ProjClass', 'Customer1'])

bill_test