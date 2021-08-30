import pickle 
from qbodbc import QB 
from qbodbc.customer import Customer

# Client application pickles an object
pickle_customer = Customer(customer="TestCustomer", account_number="CanIpickle")
pickle_file = open("pickle_customer", "wb")
pickle.dump(pickle_customer, pickle_file)
pickle_file.close()

# The pickled object is sent to some middle ware where it is 
# deserialized, and inserted into QuickBooks 

# API Server 
# Read the pickled customer from the body of a post request then: 
import pickle 
from qbodbc import QB 
from qbodbc.customer import Customer

unpickle_file = open("pickle_customer", "rb")
unpickle_customer = pickle.load(unpickle_file)
unpickle_file.close()

con = QB("qbtest")
resp = con.create(unpickle_customer)



