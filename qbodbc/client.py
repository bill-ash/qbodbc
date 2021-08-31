import pyodbc
import pandas as pd 
from .exceptions import QBCreateMethod, QBMissingTable

class QB: 
    """Connection manager"""
    def __init__(self, DSN=None, RemoteDSN=None, ip="192.168.14.143", port=4500): 
        # self.dsn = DSN
        # self.RemoteDSN = RemoteDSN
        if DSN:
            con_string = "DSN=" + DSN
        else: 
            con_string = "Driver={QRemote for QuickBooks};OLE DB Services=-2;" + "IPAddress={ip};Port={port};RemoteDSN={remote_dsn};".format(ip=ip, port=port, remote_dsn=RemoteDSN)

        print("Connecting to", con_string)
        try:
            self._connection = pyodbc.connect(
                con_string, ansi=True, autocommit=True
                )
        except Exception as e:
            print(e)
            raise Exception("Could not connect to:", con_string)
        pyodbc.pooling = False
        self._connection.setencoding(encoding='utf8')

        

    def query(self, query):
        """Raw sql returns response as a pandas df""" 
        print("Preparing query for\n", query)
        try: 
            return pd.read_sql(query, self._connection)
        except Exception as e: 
            print("Error: ", e)
            raise QBMissingTable

    def create(self, obj): 
        """Takes a QuickBooks object: customer, account, bill, jouranl entry, 
        with the _create() method implemented. 
        """
        try:
            cx = self._connection.cursor()
        # Checks the _create() method is implemented or raises an exception
            return obj._create(cx)
        except AttributeError:
            raise QBCreateMethod

    def close(self):
        """Close the connection to the current QuickBooks instance.
        Modify the DSN to prevent the current session from being closed.
        Will still close the file when opening a closed file.""" 
        self._connection.close()

    def __close__(self): 
        """Not sure which methods need to be implemented yet."""
        self.close()


# def qb_connect(dsn): 
#     try: 
#         return pyodbc.connect(dsn)
#     except Exception as e: 
#         print("Could not connect: " + e)

