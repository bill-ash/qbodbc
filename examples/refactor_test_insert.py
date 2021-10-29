from qbodbc import QuickBooks
import pytest 
from qbodbc.objects import Customer
import random

def name_generator(): 
    first_name = [
        'bob', 'marty', 'marsha', 'rasham', 'greg', 'gregory',
        'steve', 'mary', 'bill', 'suf', 'ashley', 'bently',
        'vicky', 'neria', 'moo', 'cow', 'dog', 'hary', 'fenti'
    ]
    last_name = [
        'meek', 'bills', 'type', 'popcorn', 'wordsss', 'blake'
        'blane', 'ash', 'blaire', 'world', 'fair', 'yarn', 'plow', 
        'rank', 'rafiki', 'reynolds', 'bear'
        ]

    return f"{random.choice(first_name)} {random.choice(last_name)}"

def test_insert(): 
    
    session = QuickBooks(remote_dsn="qbtest")
    
    c1 = {'Name':name_generator(), 'AccountNumber':"123321"}
    c2 = {'Name':name_generator(), 'AccountNumber':"123321"}
    c3 = {'Name':name_generator(), 'AccountNumber':"123321"}
    
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
    
    # Create a connection which returns a cursor
    # Optionally session.connect().cursor 
    # Pass the session object to all create methods
    insert_cursor = session.connect()

    session.query('select * from customer')
    session.cursor.execute('select * from customer')
    insert_cursor.execute('select * from customer').fetchall()
    
    # Helper functions from BaseObject
    cust.to_names()
    cust.to_q()
    
    # Manually create a customer 
    resp = insert_cursor.execute("""
        Insert Into Customer (name, accountnumber)
            VALUES (?, ?)
        """, cust.to_values())
    
    last_insert = session.last_insert('customer')

    cust2.to_names()
    cust2.to_values()
    cust2.to_q()

    c2_resp = insert_cursor.execute(f'insert into customer ({cust2.to_names()}) values ({cust2.to_q()})', cust2.to_values())
    last_insert = session.last_insert('customer')
        
    resp_list = [c.create(qb=session) for c in customers]
    
    session.close()


    