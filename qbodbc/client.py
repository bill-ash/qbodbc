import pyodbc
import pandas as pd 
from .exceptions import QBMissingTable

class QBConnect: 
    def __init__(self, DSN=None): 
        self.dsn = DSN if DSN else "cdata"
        con_string = "DSN=" + self.dsn
        print("Connecting to", con_string)
        self._connection = pyodbc.connect(con_string)
        pyodbc.pooling = False

    def qb_query(self, query): 
        print("Preparing query for\n", query)
        try: 
            return pd.read_sql(query, self._connection)
        except Exception as e: 
            print("Error: ", e)
            raise QBMissingTable

    def qb_close(self): 
        self._connection.close()


def qb_connect(dsn): 
    try: 
        return pyodbc.connect(dsn)
    except Exception as e: 
        print("Could not connect: " + e)

