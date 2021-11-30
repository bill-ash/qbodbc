# list mixin 
# detail mixin | filter 
# create, update, destroy mixin

class BaseObject: 
    # Add something to remove None values 
    def to_names(self): 
        """Turns object attribute names into comma seperated string to be used 
        in insert statements."""
        return ', '.join(self.__dict__.keys() if not None else next)
    
    def to_values(self): 
        """Turns object attribute values into list of values to be used in 
        insert statements."""
        return list(self.__dict__.values() if not None else next)
    
    def to_q(self): 
        """Creates a comma seperated string of question marks to be used 
        in paramterized queries. The number of question marks returns should 
        match the length of to_values()."""
        return ', '.join('?' * len(self.__dict__))

    def process_response(): 
        # Something to handle errors in a uniform manner
        pass 

    def create(self):
        q = (
            f"insert into {type(self).__name__} " 
            f"({', '.join(self.dict().keys())}) values" 
            f"({','.join('?' * len(self.dict()))})"
        )

        return q

    def update(self): 
        """
            update customer 
                set accountnumber = ?, customfield_xxx = ? 
            where listid = ? 
        """
        pass 

    def get_table(self, params):
        pass 

    def update(self): 
        pass 

    def delete(self): 
        pass 
