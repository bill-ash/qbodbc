import pytest 
from datetime import date 
from decimal import Decimal
from qbodbc.objects import Bill
from qbodbc import QuickBooks
from qbodbc.objects.bill import BillItemLine 
from tests.test_base import TestConf

insert_resp = ' '.join("""
        insert into BillItemLine 
                (ItemLineItemRefFullName, ItemLineDesc, ItemLineQuantity,
                ItemLineCost, FQSaveToCache, TxnDate, RefNumber, Memo) 
        values (?, ?, ?, ?, ?, ?, ?, ?)
""".replace('\n', '').split())

def test_bill_create():
        # Test case to get insert correct 
        line_1 = BillItemLine(Item= 'Super Cool Item',
                Desc='ItemServiceDescription', 
                Quantity=2,
                Amount=Decimal('20.21'))

        bill_test = Bill(Vendor = "Computer Store",
                APAccount = "Accounts Payable", 
                Date = date(2020, 1, 1),
                RefNumber = "12331-1231",
                Memo = "PO123312", 
                TxnDate = date(2021,1,1))

        bill_test.add_item(line_1)

        # Pop the current line item 
        test_line = bill_test._line_item.pop()
        assert isinstance(test_line, BillItemLine)
        
        # Update the child object with additional parent aruments 
        test_line.update_obj(bill_test)
        assert insert_resp == test_line.create()
        assert isinstance(test_line.to_values(), list)


def test_pre_insert():
        
        session = QuickBooks(TestConf.DSN)
        session.connect()
     
        items = session.sql('select FullName from Item where Type = ?', ['ItemService']).fetchall()
        vendor = session.sql('select Name from vendor').fetchall()
        customer = session.sql('select FullName from Customer').fetchall()
        cogs_account = session.sql('select Name from account where AccountType = ?', ['CostOfGoodsSold']).fetchall()
        class_name = session.sql('select FullName from class').fetchall()
        
        bill_test = Bill(VendorRefFullName = vendor[15][0],
                APAccountRefFullName = "Accounts Payable", 
                RefNumber = "1233-1231",
                Memo = "PO123312", 
                # ItemLineClassRefFullName = 
                TxnDate = date(2021,1,1)
                )
     

        line_1 = BillItemLine(Item=items[2][0],
                Desc='OverideAccount', 
                Quantity=2,
                ItemLineCustomerRefFullName=customer[2][0], 
                ItemLineOverrideItemAccountRefFullName=cogs_account[2][0],
                Amount=Decimal('20.21'))

        line_2 = BillItemLine(Item=items[2][0],
                Desc='Customer with normal account', 
                Quantity=2,
                ItemLineCustomerRefFullName=customer[2][0], 
                Amount=Decimal('10.21'))

        line_3 = BillItemLine(Item=items[2].FullName,
                Desc='Normal with class with amount = None', 
                Quantity=2,
                ItemLineClassRefFullName = class_name[2].FullName, 
                Amount=None
                )

        lines = [line_1, line_2, line_3]
        # Add list of items and single item 
        bill_test.add_item(line_1)
        bill_test.add_item(lines)
        
        assert len(bill_test._line_item) == 4
        

        # Create the bill 
        resp = bill_test.save(qb=session)
        last_insert = session.last_insert('BillItemLine')
        assert last_insert == resp.get('id') 


