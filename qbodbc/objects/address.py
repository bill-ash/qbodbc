from .baseobject import BaseObject

class Address(BaseObject): 

    def __init__(self, **kwargs): 
        self.BillAddressAddr1 = kwargs.pop('BillAddressAddr1', None)
        self.BillAddressAddr2 = kwargs.pop('BillAddressAddr2', None)
        self.BillAddressAddr3 = kwargs.pop('BillAddressAddr3', None)
        self.BillAddressAddr4 = kwargs.pop('BillAddressAddr4', None)
        self.BillAddressAddr5 = kwargs.pop('BillAddressAddr5', None)
        self.BillAddressCity = kwargs.pop('BillAddressCity', None)
        self.BillAddressState = kwargs.pop('BillAddressState', None)
        self.BillAddressProvince = kwargs.pop('BillAddressProvince', None)
        self.BillAddressCounty = kwargs.pop('BillAddressCounty', None)
        self.BillAddressPostalCode = kwargs.pop('BillAddressPostalCode', None)
        self.BillAddressCountry = kwargs.pop('BillAddressCountry', None)
     
        self.ShipAddressAddr1 = kwargs.pop('ShipAddressAddr1', None)
        self.ShipAddressAddr2 = kwargs.pop('ShipAddressAddr2', None)
        self.ShipAddressAddr3 = kwargs.pop('ShipAddressAddr3', None)
        self.ShipAddressAddr4 = kwargs.pop('ShipAddressAddr4', None)
        self.ShipAddressAddr5 = kwargs.pop('ShipAddressAddr5', None)
        self.ShipAddressCity = kwargs.pop('ShipAddressCity', None)
        self.ShipAddressState = kwargs.pop('ShipAddressState', None)
        self.ShipAddressProvince = kwargs.pop('ShipAddressProvince', None)
        self.ShipAddressCounty = kwargs.pop('ShipAddressCounty', None)
        self.ShipAddressPostalCode = kwargs.pop('ShipAddressPostalCode', None)
        self.ShipAddressCountry = kwargs.pop('ShipAddressCountry', None)
       
        self.Phone = kwargs.pop('Phone', None)
        self.AltPhone = kwargs.pop('AltPhone', None)
        self.Fax = kwargs.pop('Fax', None)
        self.Email = kwargs.pop('Email', None)
        self.Cc = kwargs.pop('Cc', None)
        self.Contact = kwargs.pop('Contact', None)
      