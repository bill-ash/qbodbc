# from qbodbc import QB
# import pytest 
# from qbodbc.customer import Customer
# import random

# def name_generator(): 
#     first_name = [
#         'bob', 'marty', 'marsha', 'rasham', 'greg', 'gregory',
#         'steve', 'mary', 'bill', 'suf', 'ashley', 'bently',
#         'vicky', 'neria', 'moo', 'cow', 'dog', 'hary', 'fenti'
#     ]
#     last_name = [
#         'meek', 'bills', 'type', 'popcorn', 'wordsss', 'blake'
#         'blane', 'ash', 'blaire', 'world', 'fair', 'yarn', 'plow', 
#         'rank', 'rafiki', 'reynolds', 'bear'
#         ]

#     return f"{random.choice(first_name)} {random.choice(last_name)}"

# def test_insert(): 
    
#     con_insert = QB("qbtest")
#     cust = Customer(customer=name_generator(), account_number="123321")
#     # cust = QBCustomer(customer="Wavyyyy2", account_number="123321")

#     assert type(cust.customer) == str
#     assert type(cust.account_number) == str
#     assert cust.account_number == "123321"
    
#     # con_insert._connection.execute("Insert Into Customer (Name) VALUES ('ManRespVal')")
#     # cust.job()

#     cust_resp = con_insert.create(cust)
#     cust_resp_error = con_insert.create(cust)
    
#     con_insert.close()


    