class QuickBooksError(Exception): 
    pass 

class QBConnectionError(QuickBooksError): 
    pass 

class QBMissingTable(QuickBooksError): 
    pass 

class QBCreateMethod(QuickBooksError):
    pass