import pytest 
from datetime import date 
from decimal import Decimal
from qbodbc.objects import Bill
from qbodbc.objects.bill import BillItemLine 


# Test case to get insert correct 
line_1 = BillItemLine(Item= 'Super Cool Item',
        Desc='ItemServiceDescription', 
        Quantity=2,
        Amount=Decimal('20.21'))

line_1.to_dict()
line_1.to_values()
bill_test = Bill(Vendor = "Computer Store", APAccount = "Accounts Payable", 
        Date = date(2020, 1, 1), RefNumber = "12331-1231", Memo = "PO123312", 
        TxnDate = date(2021,1,1))

bill_test.add_item(line_1)
bill_test.to_dict()
bill_test.to_values()

# Pop the current line item 
test_line = bill_test._line_item.pop()

# Update the child object with additional parent aruments 
test_line.update_obj(bill_test)
test_line.create()
test_line.to_values()

bill_test.save()


