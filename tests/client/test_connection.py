import pytest
from qbodbc import QuickBooks 
from qbodbc.exceptions import QBMissingTable

def test_connection(): 
    con = QuickBooks('qbtest')
    con.connect()
    customer = con.query('SELECT * FROM Customer')
    
    with pytest.raises(QBMissingTable) as e_info: 
        error = con.query("SELECT * FROM Missing")
    
    con.close()

def test_connection_error():     
    with pytest.raises(Exception):
        error_con = QuickBooks("MissingFile").connect()

def test_query(): 
    
    qb = QuickBooks(remote_dsn='qbtest')
    qb.connect()

    qb.tables()
    qb.last_insert('Customer')
    qb.cursor.execute('sp_tables')
    qb.cursor.fetchone()
 
def test_call():
    con = QuickBooks("qbtest")
    con.connect()
    account = con.query("SELECT * FROM Account")
    assert len(account) > 1
    con.close()