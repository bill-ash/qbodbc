import requests
from qbodbc.objects import Customer
import json 
base_url = 'http://localhost:5000'

body = {
    'customer': {
        'FullName': 'Harry'
    },
    'customer': {
        'FullName': 'Marry'
    }
}

customer = Customer()
json.dumps(customer.__dict__)
requests.post(base_url + '/customer/customers', json=body)