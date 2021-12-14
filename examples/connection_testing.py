import pyodbc
# Forces file closed on con.close()
pyodbc.pooling=False

cnxn = pyodbc.connect('DSN=qbtest')
# Set encoding 
cnxn.setencoding(encoding='utf-8')

# Show the current connected dsn 
# cnxn.getinfo(pyodbc.SQL_DATA_SOURCE_NAME)
# Shows 0 for qodbc 
# cnxn.getinfo(pyodbc.SQL_MAX_CONCURRENT_ACTIVITIES)

# Create cursors independently for concurrent queries 
cursor = cnxn.cursor()
cursor.execute("Insert into Customer (Name) values ('mrharrypotter3211')")

# pyodbc cursor attributes 
cursor.tables(table='Customer')
cursor.columns(table='Customer')
cursor.statistics(table='Customer')
cursor.rowIdColumns(table='Customer')
cursor.primaryKeys(table='Customer')
cursor.getTypeInfo(table='Customer')

cursor.execute("SELECT * FROM Customer WHERE Name=?", 'mrharrypotter3211')
# Fetch the next row in the cursor 
row = cursor.fetchone()

# Call collumns using dot notation - update objects like: 
# customer.get() # return a customer 
# customer.FullName = 'Updated Name'
# customer.update() # update the instance of customer with new value  
row.FullName
row.Name = 'mrharrypotter2332131'
row.ListID
row.cursor_description

# Use parameterized queries to insert new data 
cursor.execute("update customer set Name=? where FullName=?", row.Name, row.FullName)

print('columns:', ', '.join(t[0] for t in row.cursor_description))

cursor.execute("""
    insert into customer (Name)
        values (?)
        """, ['NewValue'])

# Number of rows efected 
cursor.rowcount

# qodbc stored procedure 
cursor.execute("""
    sp_lastinsertid Customer
    """)

# pyodbc returns the first value in the first row 
cursor.fetchval() # == cursor.fetchone()[0].ID

# ID of the last customer added 
cursor.fetchone()

# Close the instance of cursor 
cursor.close()

# Close a connection - closes file 
cnxn.close()

# Query tables with multiple cursors 
cnxn = pyodbc.connect('DSN=qbtest')
cursor = cnxn.cursor()

# Can be assigned to an object or called on itself cursor.fetch*
customer = cursor.execute("SELECT * FROM Customer")
row = cursor.fetchone()

customer.fetchone() # tuple
customer.fetchmany(10) # list of tuples 
customer.fetchall() # list of tuples all remaining values 
cursor.close() 

# Start a second cursor after closing the first 
cursor2 = cnxn.cursor()
cursor2.execute('SELECT * FROM Account')

cursor2.fetchone()

cursor2.close()
cnxn.close()
