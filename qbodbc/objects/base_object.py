# list mixin 
# detail mixin | filter 
# create, update, destroy mixin
# from qbodbc.client import Client

def to_dict(obj, classkey=None):
    """
    Recursively converts Python object into a dictionary
    Stolen from: https://github.com/ej2/python-quickbooks/blob/c82935bd07d9901d0e8d10765a7fcb06ad2ef53d/quickbooks/mixins.py#L89
    """
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return to_dict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [to_dict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, to_dict(value, classkey))
                    for key, value in obj.__dict__.items()
                    if not callable(value) and not key.startswith('_')])

        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj

class ToDictMixin:
    def to_dict(self):
        return to_dict(self)


class BaseObject(ToDictMixin): 
           
    def to_names(self): 
        """
        Turns object attribute names into comma seperated string to be used 
        in insert statements.
        """
        return ', '.join([key for key, value in self.to_dict().items() if value is not None])
    
    def to_values(self): 
        """
        Turns object attribute values into list of values to be used in 
        insert statements.
        """
        return [value for key, value in self.to_dict().items() if value is not None]
    
    def to_params(self): 
        """
        Creates a comma seperated string of question marks to be used 
        in paramterized queries. The number of question marks returns should 
        match the length of to_values().
        """
        return ', '.join('?' * len([key for key, value in self.to_dict().items() if value is not None]))

    def update_obj(self, obj):
        """
        Merge a child object with its parent or vica versa. 
        """
        for k, v in obj.to_dict().items():
            if v:
                if v is not None:
                    setattr(self, k, v) 

    def process_response(): 
        # Something to handle errors in a uniform manner
        pass 

    def create(self):
        q = (
            f"insert into {self.__table_name__} " 
                f"({self.to_names()}) values " 
            f"({self.to_params()})"
        )

        return q

    # def update(self): 
    #     """
    #         update customer set 
    #             accountnumber = ?, customfield_xxx = ? 
    #         where listid = ? 
    #     """
    #     pass 


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

