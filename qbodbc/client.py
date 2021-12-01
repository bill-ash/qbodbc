import logging 
from pprint import pprint 

import pandas as pd 
import pyodbc
from .exceptions import (
    QuickBooksError, QBCreateMethod, QBMissingTable, QBConnectionError
)


class QuickBooks: 
    pyodbc.pooling = False

    def __init__(self, DSN=None, remote_dsn=None, ip='', port=4500): 
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
        """Initialize the connection and set the curor to be used in all calls.""" 
        try:
            if self.cnxn is None:
                logging.info('Connecting to: ', self.connection_string)
                self.cnxn = pyodbc.connect(self.connection_string, ansi=True, autocommit=True)
                self.cnxn.setencoding(encoding='utf-8')
                self.cursor = self.cnxn.cursor()
            else: 
                """Reconnect"""
                self.cursor = self.cnxn.cursor()

        except Exception as e:
            raise QBConnectionError('Could not connect to: ', self.connection_string)


    def query(self, query):
        """Raw sql returns response as a pandas df""" 
        logging.info("Preparing query for\n", query)
        try: 
            return pd.read_sql(query, self.cnxn)
        except Exception as e: 
            raise QBMissingTable('Not a table...')

    def sql(self, sql, params=[]):
        """Execute some raw sql. Params passes as a list."""
        return self.cursor.execute(sql, params)

    def last_insert(self, table): 
        """Fetch last insert"""
        return self.cursor.execute(f'sp_lastinsertid {table}').fetchval()

    def columns(self, table): 
        return self.query(f'sp_columns {table}')[
            ['COLUMNNAME', 'TYPENAME', 'NULLABLE',
       'REMARKS', 'DEFAULT', 'DATATYPE', 'DATETIME_SUBTYPE',
       'ORDINAL_POSITION', 'IS_NULLABLE', 'QUERYABLE', 'UPDATEABLE',
       'INSERTABLE', 'REQUIRED_ON_INSERT', 'FORMAT', 'RELATES_TO',
       'JUMPIN_TYPE', 'CUSTOM_FIELD_NAME']
        ]


    def primary_keys(self, table): 
        return self.cursor.execute(f'sp_primarykeys {table}').fetchall()
    
    
    def optimize_full_sync(self, table=None):
        if table is None: 
            table = 'all'
        self.cursor.execute('sp_optimizefullsync {table}')

    def tables(self): 
        cc = [list((c[2], c[4])) for c in self.cursor.execute('sp_tables').fetchall()]
        print(*cc, sep='\n')
    
    
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