from qbodbc import QB 

# Connect to the file defined in the qbtest configuration 
con = QB(DSN='qbtest')

# Query some tables 
customers = con.query('SELECT * FROM Customer')
accounts = con.query('SELECT * FROM Account')


# Close the connection 
# Adjust settings in qodbc to force close application
con.close()

# Connect without DSN: 
# Standard syntax
# "Driver={QRemote for QuickBooks};OLE DB Services=-2;IPAddress=127.0.0.1;Port=4500;"
# con_string = "Driver={QRemote for QuickBooks};OLE DB Services=-2;IPAddress=192.168.14.143;Port=4500;RemoteDSN=qbtest;"
 
from qbodbc import QB

con = QB(RemoteDSN="qbtest")

customer = con.query("SELECT * FROM Customer")
accounts = con.query("SELECT * FROM Account")

con.close()
