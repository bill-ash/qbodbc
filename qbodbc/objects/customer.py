from typing import Optional
from .baseobject import BaseObject
from qbodbc.client import QuickBooks

# Turn session into cls object and pass to 
# objects directly?
 
class Customer(BaseObject):

    __table_name__ = 'customer'
    
    def __init__(self, **kwargs):
        """Customer Model:
        Initialize a customer with the minimum requirements.
        """
        self.Name=kwargs.pop('Name', None)
        self.AccountNumber= kwargs.pop('AccountNumber', None)
        # self.first_name=first_name
        # self.last_name=last_name

    def job(self, job):
        """Create a job for the specific customer."""
        self.job = job

    def create(self, qb):
        """Create the Customer and Customer Job in one step. If the 
        Customer already exists, create the job. Response object is the
        created values + guids."""
        try:
            qb.sql(f"insert into customer ({ self.to_names() }) values ({ self.to_q() })",
                self.to_values())
                
            return {
                "id": qb.last_insert('customer'),
                "key": self.Name
            }

        except Exception as e:
            return {
                "id": e.args[-1],
                "key": self.Name
            }
    
    def __repr__(self): 
        return self.Name if self.Name is None else ''