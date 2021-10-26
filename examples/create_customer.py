from qbodbc import QB
from qbodbc.customer import Customer

def random_string():
    import random 
    return str(random.randint(20000, 30000))

# Connect to the file defined by qbtest DSN 
qb_con = QB("qbtest")

# Create a single customer 
client = "SUPERHERO" + random_string()

test_customer = Customer(client, "33211")

cust_resp = qb_con.create(test_customer)

# Update optimizer setting to optimize after each insert/ update
customer = qb_con.query("SELECT * FROM Customer")

# Adjust optimizer settings to make the insert available immediately 
assert client == customer[customer['Name'] == client]['Name'][0]

# Count the number of customers 
len(customer)

# Create many customers 
list_of_customers = ["ben", "jerry", "susan", "barry"]
list_of_customers = [c + random_string() for c in list_of_customers]

resp = []

for i in list_of_customers: 
    c = Customer(i, random_string())
    print(c)
    c_resp = qb_con.create(c)
    resp.append(c_resp)

# Insepct the response [{ID, CustomerName}]
resp


# Cause an exception 
cust_error = Customer("This is a really long customer name that will cause an issue")
qb_con.create(cust_error)


# Close the connection
qb_con.close()

