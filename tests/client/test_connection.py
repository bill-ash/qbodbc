import pytest
import pandas as pd 
from pyodbc import Connection, Cursor, Row

from qbodbc import QuickBooks 
from qbodbc.exceptions import QBMissingTable, QBConnectionError
from tests.test_base import TestConf


def test_connection(): 
    session = QuickBooks(TestConf.DSN)
    session.connect()
    
    customer = session.query('SELECT * FROM Customer')
    assert isinstance(customer, pd.DataFrame)
    account = session.query('SELECT * FROM Account')
    assert isinstance(account, pd.DataFrame)
    
    with pytest.raises(QBMissingTable) as e_info: 
        error = session.query("SELECT * FROM Missing")
    
    session.close()

def test_connection_error():     
    with pytest.raises(QBConnectionError):
        error_con = QuickBooks("MissingFile").connect()

def test_session(): 
    session = QuickBooks(TestConf.DSN)
    session.connect()
    assert isinstance(session.cnxn, Connection)
    assert isinstance(session.cursor, Cursor)
    session.close()


def test_query(): 
    session = QuickBooks(remote_dsn=TestConf.DSN, ip=TestConf.IP)
    session.connect()

    resp = session.sql('select * from account', [])
    resp.columns().fetchone()
    resp_all = resp.fetchall()
    
    assert isinstance(resp_all, list)
    assert isinstance(resp.columns().fetchone(), Row)
    session.close()

def test_expense_query(): 
    session = QuickBooks(TestConf.DSN)
    session.connect()

    resp = session.sql('select * from account where accounttype = ?', ['expense'])
    
    assert isinstance(resp.fetchone(), Row)
    expense_row = resp.fetchone()
    assert expense_row.AccountType == 'Expense'
    assert isinstance(expense_row.ListID, str)
    session.close()

def test_methods():
    session = QuickBooks(TestConf.DSN)
    session.connect()

    tables = session.tables()
    
    session.cursor.execute('SELECT * FROM Customer')
    
    resp = session.sql('select * from Customer where isactive = ?', [True])
    row_customer = resp.fetchone()
    assert row_customer.IsActive

    resp = session.sql('select * from Customer where isactive = ?', [1])
    row_customer = resp.fetchone()
    assert row_customer.IsActive

 
def test_call():
    con = QuickBooks(TestConf.DSN)
    con.connect()
    account = con.query("SELECT * FROM Account")
    assert len(account) > 1
    con.close()