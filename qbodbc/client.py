from pprint import pprint 
import pyodbc
import pandas as pd 
from .exceptions import QBCreateMethod, QBMissingTable

class QuickBooks: 
    pyodbc.pooling = False

    def __init__(self, DSN=None, remote_dsn=None, ip="192.168.14.143", port=4500): 
        """Create a local or remote connection"""
        if DSN:
            self.connection_string = ("DSN=" + DSN)
        else: 
            self.connection_string = ';'.join([
                "Driver={QRemote for QuickBooks}",
                f"IPAddress={ip}",
                f"Port={port}",
                f"RemoteDSN={remote_dsn};"
            ])
        self.cnxn = None
        self.cursor = None


    def connect(self): 
        try:
            if self.cnxn is None:
                print("Connecting to", self.connection_string)
                self.cnxn = pyodbc.connect(
                    self.connection_string, ansi=True, autocommit=True
                    )
                self.cnxn.setencoding(encoding='utf-8')
                self.cursor = self.cnxn.cursor()
                return self.cursor
            else: 
                return self.cnxn.cursor()

        except Exception as e:
            print(e)
            raise Exception("Could not connect to:", self.connection_string)


    def query(self, query):
        """Raw sql returns response as a pandas df""" 
        print("Preparing query for\n", query)
        try: 
            return pd.read_sql(query, self.cnxn)
        except Exception as e: 
            print("Error: ", e)
            raise QBMissingTable

    def sql(self, sql, params):
        return self.cursor.execute(sql, params)

    def last_insert(self, table): 
        return self.cursor.execute(f'sp_lastinsertid {table}').fetchval()


    def table_columns(self, table): 
        return self.query(f'sp_columns {table}')[
            ['tablename', 'columnname', 'type', 'typename', 'remarks', 'default',
            'datatype', 'is_nullable','updateable', 'insertable', 'required_on_insert',
            'format', 'realtes_to', 'jumpin_type', 'custom_field_name'
            ]
        ]


    def primary_keys(self, table): 
        return self.cursor.execute(f'sp_primarykeys {"table"}').fetchall()
    
    
    def optimize_full_sync(self, table=None):
        if table is None: 
            table = 'all'
        self.cursor.execute('sp_optimizefullsync {table}')

    def tables(self): 
        cc = [list((c[2], c[4])) for c in self.cursor.execute('sp_tables').fetchall()]
        pprint(cc, width=200)
    
    
    def file_name(self): 
        return self.cursor.execute('sp_qbfilename').fetchval()


    def delete(self, table, transaction_id): 
        return self.cursor.execute(f'sp_void {table} where TxnID = ?', transaction_id).fetchval()


    def close(self):
        """Close the connection to the current QuickBooks instance.
        Modify the DSN to prevent the current session from being closed.
        Will still close the file when opening a closed file.""" 
        self.cnxn.close()

    def __close__(self): 
        """Not sure which methods need to be implemented yet."""
        self.cnxn.close()


    # def create(self, obj): 
    #     """Takes a QuickBooks object: customer, account, bill, jouranl entry, 
    #     with the _create() method implemented. 
    #     """
    #     try:
    #         cx = self.cnxn()
    #     # Checks the _create() method is implemented or raises an exception
    #         return obj._create(cx)
    #     except AttributeError:
    #         raise QBCreateMethod