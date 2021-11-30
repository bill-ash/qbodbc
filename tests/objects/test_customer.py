import random
import pytest
from datetime import datetime 
from tests.test_base import TestConf
from qbodbc import QuickBooks
from qbodbc.objects import Customer
from qbodbc.utils import name_generator, account_generator
from pyodbc import ProgrammingError

def test_insert(): 
    
    c1 = {'Name':name_generator(), 'AccountNumber':'123321'}
    c2 = {'Name':name_generator(), 'AccountNumber':account_generator()}
    c3 = {'Name':name_generator(), 'AccountNumber':account_generator(), 'Phone': '2313211232'}
    
    cust = Customer(**c1)

    cust1 = Customer()
    cust1.Name = c2.get('Name')
    cust1.AccountNumber = c2.get('AccountNumber')
    
    cust2 = Customer()
    [setattr(cust2, k, v) for k,v in c3.items()]
    
    customers = [cust, cust1, cust2]
    
    assert type(cust.Name) == str
    assert type(cust.AccountNumber) == str
    assert cust.AccountNumber == "123321"

    # Create a session object - session object gets passed to the table object
    session = QuickBooks(TestConf.DSN)
    session.connect()

    session.query('select * from customer')
    session.cursor.execute('select * from customer')
    
    
    # Manually create a customer - need to manually retreive the result
    resp = session.cursor.execute("""
        Insert Into Customer (name, accountnumber)
            VALUES (?, ?)
        """, ['McHarry' + datetime.now().strftime('%y%m%d%H%M%S'), '123321123'])
    
    with pytest.raises(ProgrammingError):
        resp.fetchval()
    
    # ListId of the last created object 
    resp = session.last_insert('Customer')
    assert isinstance(resp, str)

    # Pass all args as strings 
    session.cursor.execute(f'insert into customer ({cust2.to_names()}) values ({cust2.to_params()})', cust2.to_values())
    last_insert = session.last_insert('customer')
    assert isinstance(last_insert, str)

    # When using the save method the last insert and primary key are returned 
    resp_list = [c.save(qb=session) for c in customers]
    
    session.close()



    