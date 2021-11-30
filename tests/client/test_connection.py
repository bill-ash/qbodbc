import pytest
from qbodbc import QuickBooks 
from qbodbc.exceptions import QBMissingTable
import pandas as pd 


def test_connection(): 
    quick_books = QuickBooks('qbtest')
    quick_books.connect()
    
    customer = quick_books.query('SELECT * FROM Customer')
    assert isinstance(customer, pd.DataFrame)
    

    with pytest.raises(QBMissingTable) as e_info: 
        error = quick_books.query("SELECT * FROM Missing")
    
    quick_books.close()

def test_connection_error():     
    with pytest.raises(Exception):
        error_con = QuickBooks("MissingFile").connect()



def test_query(): 
    
    qb = QuickBooks(remote_dsn='qbtest')
    qb.connect()

    qb.tables()
    x = None
    qb.cursor.execute('SELECT * FROM Customer')
    
    qb.sql('SELECT * FROM Customer WHERE Name = ?', 'HarryPotter')
    qb.fetchone()
    qb.last_insert('Customer')
    qb.cursor.execute('sp_tables')
    qb.cursor.fetchone()
 
def test_call():
    con = QuickBooks("qbtest")
    con.connect()
    account = con.query("SELECT * FROM Account")
    assert len(account) > 1
    con.close()