import pyodbc
import pandas as pd 
from .exceptions import QBCreateMethod, QBMissingTable

class QBConnect: 
    """Connection manager"""
    def __init__(self, DSN=None): 
        self.dsn = DSN if DSN else "cdata"
        con_string = "DSN=" + self.dsn
        print("Connecting to", con_string)
        self._connection = pyodbc.connect(con_string)
        pyodbc.pooling = False

    def qb_query(self, query):
        """Raw sql returns response as a pandas df""" 
        print("Preparing query for\n", query)
        try: 
            return pd.read_sql(query, self._connection)
        except Exception as e: 
            print("Error: ", e)
            raise QBMissingTable

    def qb_create(self, obj): 
        """Takes a QuickBooks object: customer, account, bill, jouranl entry, 
        with the _create() method implemented. 
        """
        try:
            cx = self._connection.cursor()
            return obj._create(connection = cx)
        # Checks the _create() method is implemented or raises an exception
        except AttributeError:
            raise QBCreateMethod

    def qb_close(self):
        """Close the connection to the current QuickBooks instance.
        Modify the DSN to prevent the current session from being closed.
        Will still close the file when opening a closed file.""" 
        self._connection.close()


# def qb_connect(dsn): 
#     try: 
#         return pyodbc.connect(dsn)
#     except Exception as e: 
#         print("Could not connect: " + e)

