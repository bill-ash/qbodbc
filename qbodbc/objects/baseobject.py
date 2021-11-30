# list mixin 
# detail mixin | filter 
# create, update, destroy mixin
# from qbodbc.client import Client

class BaseObject: 
    # Add something to remove None values 
    def to_names(self): 
        """
        Turns object attribute names into comma seperated string to be used 
        in insert statements.
        """
        return ', '.join([key for key, value in self.__dict__.items() if value is not None])
    
    def to_values(self): 
        """
        Turns object attribute values into list of values to be used in 
        insert statements.
        """
        return [value for key, value in self.__dict__.items() if value is not None]
    
    def to_params(self): 
        """
        Creates a comma seperated string of question marks to be used 
        in paramterized queries. The number of question marks returns should 
        match the length of to_values().
        """
        return ', '.join('?' * len([key for key, value in self.__dict__.items() if value is not None]))

    def process_response(): 
        # Something to handle errors in a uniform manner
        pass 

    def create(self):
        q = (
            f"insert into {self.__table_name__} " 
            f"({self.to_names()}) values" 
            f"({self.to_params()})"
        )

        return q

    def update(self): 
        """
            update customer set 
                accountnumber = ?, customfield_xxx = ? 
            where listid = ? 
        """
        pass 


    def delete(self): 
        pass 


    def save(self, qb):
        """
        Create or update
        Args: 
            qb: session object, instance of QuickBooks().connect().
        """
        try:
            qb.cursor.execute(self.create(), self.to_values())
                
            return {
                "id": qb.last_insert(self.__table_name__),
                "key": self.to_ref.Value
            }

        except Exception as e:
            return {
                "id": e.args[-1],
                "key": self.to_ref.Value
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

