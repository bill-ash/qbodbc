import pytest
from qbodbc import QB
from qbodbc.exceptions import QBMissingTable

def test_connection(): 
    con = QB('qbtest')
    customer = con.query('SELECT * FROM Customer')
    
    with pytest.raises(QBMissingTable) as e_info: 
        error = con.query("SELECT * FROM Missing")
    
    con.close()

def test_connection_error():     
    with pytest.raises(Exception):
        error_con = QB("MissingFile")


# def test_call():
#     con = QB("qbtest")
#     account = con.query("SELECT * FROM Account")
#     assert len(account) > 1
#     con.close()