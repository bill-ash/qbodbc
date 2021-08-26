
class Customer:
    def __init__(self, customer, account_number=''):
        """Customer Model:
        Initialize a customer with the minimum requirements.
        """
        self.customer=customer
        self.account_number=account_number
        # self.first_name=first_name
        # self.last_name=last_name

    def job(self, job):
        """Create a job for the specific customer."""
        self.job = job

    def _create(self, connection):
        """Create the Customer and Customer Job in one step. If the 
        Customer already exists, create the job. Response object is the
        created values + guids."""
        resp = {}
        q = f"""Insert Into Customer (Name, AccountNumber) VALUES ('{self.customer}', '{self.account_number}')"""
        try:
            connection.execute(q)
            return {
                "id": connection.execute("sp_lastinsertid Customer").fetchone()[0],
                "customer": self.customer
            }
        except Exception as e:
            print("Error:", e)
            return {
                "id": e.args[-1],
                "customer": self.customer
            }
            
        # connection.last_insert()
        
        # if self.job: 
        #     j = f"""Insert Into Customer (ParentRefFullName, Name) VALUES ('{self.customer}', '{self.job}')"""
        #     connection.execute(q)
        #     resp.append(connection.execute("sp_lastinsertid Customer"))
            # connection.last_insert()
        # return resp
    
    def __repr__(self): 
        return self.customer