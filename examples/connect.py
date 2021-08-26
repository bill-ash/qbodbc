from qbodbc import QB 

# Connect to the file defined in the qbtest configuration 
con = QB('qbtest')

# Query some tables 
customers = con.query('SELECT * FROM Customer')
accounts = con.query('SELECT * FROM Account')


# Close the connection 
#  - Will not force close an active session
#  - Will open file in background
con.close()
