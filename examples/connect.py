from qbodbc import QuickBooks
from qbodbc.objects import Customer

# Connect to the file defined in the qbtest configuration 
con = QuickBooks(DSN='qbtest')
cursor = con.connect()

# Each call still needs to be made independently?
# threading to execute each simultaneously?
customer = con.cnxn.execute("SELECT * FROM Customer")
customer.fetchone()

cursor.execute("SELECT * FROM Customer")
row = cursor.fetchone()
cursor.close()
con.close()

row.cursor_description 

con = QuickBooks(remote_dsn='qbtest')
con.connect()
con.cnxn.execute("insert into customer (Name) values ('BillBenning')")
con.cnxn.execute('SP_lastinsertid customer').fetchone()
con.close()


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
from qbodbc.objects import Customer
customer = Customer(Name='MySuperName', AccountNumber='2312')
customer.create()
