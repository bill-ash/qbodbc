from typing import Optional

from .baseobject import BaseObject
from .address import Address
# Turn session into cls object and pass to 
# objects directly?
 
class Customer(Address, BaseObject):

    __table_name__ = 'customer'
    
    def __init__(self, **kwargs):
        """Customer Model:
        Initialize a customer with the minimum requirements.
        """
        super(Customer, self).__init__(**kwargs)
        self.Name=kwargs.pop('Name', None)
        self.AccountNumber= kwargs.pop('AccountNumber', None)
        self.CompanyName = kwargs.pop('CompanyName', None)
        self.FirstName = kwargs.pop('FirstName', None)
        self.MiddleName = kwargs.pop('MiddleName', None)
        self.LastName = kwargs.pop('LastName', None)
        self.JobTitle = kwargs.pop('JobTitle', None) 
        self.CustomerTypeRefFullName = kwargs.pop('CustomerTypeRefFullName', None)
        self.TermsRefFullName = kwargs.pop('TermsRefFullName', None)
        self.SalesRepRefFullName = kwargs.pop('SalesRepRefFullName', None)
        self.ResaleNumber = kwargs.pop('ResaleNumber', None)
        self.AccountNumber = kwargs.pop('AccountNumber', None)
        self.BusinessNumber = kwargs.pop('BusinessNumber', None)
        self.CreditLimit = kwargs.pop('CreditLimit', None)
        self.JobStatus = kwargs.pop('JobStatus', None)
        self.JobStartDate = kwargs.pop('JobStartDate', None)
        self.JobProjectedEndDate = kwargs.pop('JobProjectedEndDate', None)
        self.JobEndDate = kwargs.pop('JobEndDate', None)
        self.JobDesc = kwargs.pop('JobDesc', None)
        self.JobTypeRefListID = kwargs.pop('JobTypeRefListID', None)
        self.JobTypeRefFullName = kwargs.pop('JobTypeRefFullName', None)
        self.Notes = kwargs.pop('Notes', None)
        self.ExternalGUID = kwargs.pop('ExternalGUID', None)
        #  'FullName',
        #  'IsActive',
        #  'Salutation',
        #  'CustomerTypeRefListID',
        #  'TermsRefListID',
        #  'SalesRepRefListID',
        #  'Balance',
        #  'TotalBalance',
        #  'OpenBalance',
        #  'OpenBalanceDate',
        #  'SalesTaxCodeRefListID',
        #  'SalesTaxCodeRefFullName',
        #  'TaxCodeRefListID',
        #  'TaxCodeRefFullName',
        #  'ItemSalesTaxRefListID',
        #  'ItemSalesTaxRefFullName',
        #  'SalesTaxCountry',
        #  'PreferredPaymentMethodRefListID',
        #  'PreferredPaymentMethodRefFullName',
        #  'CreditCardInfoCreditCardNumber',
        #  'CreditCardInfoExpirationMonth',
        #  'CreditCardInfoExpirationYear',
        #  'CreditCardInfoNameOnCard',
        #  'CreditCardInfoCreditCardAddress',
        #  'CreditCardInfoCreditCardPostalCode',
        #  'PreferredDeliveryMethod',
        #  'IsUsingCustomerTaxCode',
        #  'PriceLevelRefListID',
        #  'PriceLevelRefFullName',
        #  'TaxRegistrationNumber',
        #  'CurrencyRefListID',
        #  'CurrencyRefFullName'
        

    def job(self, job):
        """Create a job for the specific customer."""
        self.job = job

    

    def save(self, qb):
        """
        Response object is the created values + guids.
        Args: 
            qb: session object, instance of QuickBooks().connect().
        """
        try:
            qb.cnxn.execute(
                    f"insert into customer ({ self.to_names() }) \
                        values ({ self.to_q() })",
                    self.to_values()
                )
                
            return {
                "id": qb.last_insert('customer'),
                "key": self.Name
            }

        except Exception as e:
            return {
                "id": e.args[-1],
                "key": self.Name
            }
    

    # Should all be passed as mixins to the base object. 
    def get(self, qb): 
        """
        Returns one or None. To be used in updates. 
        """
        pass 

    def all(self, qb, params): 
        """
        Gets the entire table. Takes optional param of column names to return. 
        """
        pass 
    
    def filter(self, qb, params): 
        """
        Return a subset of customers that meet certian conditions. 
        """
        pass 