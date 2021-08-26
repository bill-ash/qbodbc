from qbodbc.utils import *
from qbodbc.bill import Bill
from qbodbc import QB

qb_con = QB("qbtest")


qb_con._connection.execute("sp_columns Bill").fetchall()

qb_con._connection.execute("SELECT * FROM Bill").fetchall()

cursorb = qb_con._connection.cursor().execute("SELECT * FROM Bill")




bill_args = qb_con.query("sp_columns Bill")

bill_args[bill_args["IS_NULLABLE"] == "YES"][["COLUMNNAME", "TYPENAME"]]

Bill.get_args(qb_con)

qb_con.query("SELECT * FROM Bill")
qb_con.query("sp_columns Bill")[['TABLENAME', 'COLUMNNAME', 'TYPENAME']]

print("hello")
qb_con.close()