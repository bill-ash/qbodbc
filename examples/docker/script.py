from qbodbc import QB 
import time

con = QB(RemoteDSN="qbtest")

customers = con.query("SELECT * FROM Customer")

customers 

con.close()

time.sleep(4)

print("End")