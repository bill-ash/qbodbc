import pytest
import qbodbc
from qbodbc.exceptions import QBMissingTable

def test_connection(): 

    zz = qbodbc.QBConnect('qbtest')
    # customer = zz.qb_query('SELECT * FROM Customer')
    # payment = zz.qb_query("SELECT * FROM ReceivePaymentLine")

    with pytest.raises(QBMissingTable) as e_info: 
        error = zz.qb_query("SELECT * FROM Missing")
    
    zz.qb_close()


def test_call():

    zz = qbodbc.QBConnect("qbtest")
    account = zz.qb_query("SELECT * FROM Account")
    assert len(account) > 1
    
    zz.qb_close()