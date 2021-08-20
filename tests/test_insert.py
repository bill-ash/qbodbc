from qbodbc.client import QBConnect
import pytest 
import qbodbc
from qbodbc.customers import QBCustomer
import random

def name_generator(): 
    first_name = ['bob', 'steve', 'mary', 'bill', 'suf', 'ashley', 'bently']
    last_name = ['meek', 'bills', 'type', 'popcorn', 'wordsss', 'blake']

    return f"{random.choice(first_name)} {random.choice(last_name)}"

def test_insert(): 
    z = qbodbc.QBConnect("qbtest")
    cust = QBCustomer(customer=name_generator(), account_number="123321")
    # cust = QBCustomer(customer="Wavyyyy2", account_number="123321")

    assert type(cust.customer) == str
    assert type(cust.account_number) == str
    assert cust.account_number == "123321"
    
    # z._connection.execute("Insert Into Customer (Name) VALUES ('ManRespVal')")
    # cust.job()

    cust_resp = z.qb_create(cust)
    cust_resp_error = z.qb_create(cust)
    
    z.qb_close()


    