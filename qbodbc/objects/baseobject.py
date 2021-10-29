
class BaseObject: 
    # Add something to remove None values 
    def to_names(self): 
        return ', '.join(self.__dict__.keys())
    
    def to_values(self): 
        return list(self.__dict__.values())
    
    def to_q(self): 
        return ', '.join('?' * len(self.__dict__))

    def from_dict(self): 
        pass 

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

    def get_table(self, params):
        pass 

    def update(self): 
        pass 

    def delete(self): 
        pass 
