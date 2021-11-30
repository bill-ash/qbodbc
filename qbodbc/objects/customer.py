from qbodbc.objects.address import Address
from qbodbc.objects.base_object import BaseObject
from qbodbc.utils import Ref

class Customer(BaseObject, Address): 

    __table_name__ = 'customer'
    __table_id__ = 'Name'
    
    def __init__(self, **kwargs):
        """
        Customer Model:
            Initialize a customer with the minimum requirements.
        """
        super(Customer, self).__init__(**kwargs)
        self.Name=kwargs.pop('Name', None)
        self.AccountNumber=kwargs.pop('AccountNumber', None)
        self.CompanyName=kwargs.pop('CompanyName', None)
        self.FirstName=kwargs.pop('FirstName', None)
        self.MiddleName=kwargs.pop('MiddleName', None)
        self.LastName=kwargs.pop('LastName', None)
        self.JobTitle=kwargs.pop('JobTitle', None) 
        self.CustomerTypeRefFullName=kwargs.pop('CustomerTypeRefFullName', None)
        self.TermsRefFullName=kwargs.pop('TermsRefFullName', None)
        self.SalesRepRefFullName=kwargs.pop('SalesRepRefFullName', None)
        self.ResaleNumber=kwargs.pop('ResaleNumber', None)
        self.BusinessNumber=kwargs.pop('BusinessNumber', None)
        self.CreditLimit=kwargs.pop('CreditLimit', None)
        self.JobStatus=kwargs.pop('JobStatus', None)
        self.JobStartDate=kwargs.pop('JobStartDate', None)
        self.JobProjectedEndDate=kwargs.pop('JobProjectedEndDate', None)
        self.JobEndDate=kwargs.pop('JobEndDate', None)
        self.JobDesc=kwargs.pop('JobDesc', None)
        self.JobTypeRefListID=kwargs.pop('JobTypeRefListID', None)
        self.JobTypeRefFullName=kwargs.pop('JobTypeRefFullName', None)
        self.Notes=kwargs.pop('Notes', None)
        self.ExternalGUID=kwargs.pop('ExternalGUID', None)
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
        
    @property 
    def to_ref(self):
        ref = Ref()
        ref.Name = 'Name'
        ref.Value = self.Name
        return ref

    def job(self, job):
        """
        Create a customer or query a customer to use as a ref with to_ref()
        """
        ...

    def __str__(self): 
        return self.Name