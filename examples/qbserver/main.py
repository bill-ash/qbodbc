from qbodbc import QuickBooks
from qbodbc.objects import Customer

from fastapi import FastAPI, Body
import uvicorn 

app = FastAPI()

@app.get("/")
def root(): 
    return "Hello World!"

# When embed == True {'customer': {'id':'123', ...}}
# else  {'id':'123', ...}
@app.post("/customer/customers")
def customer_create(customer=Body(..., embed=True)): 
    
    # con = QB('qbtest')
    # customer = Customer.from_json(**customer)
    # resp = customer.create()
    # con.close()
    # return resp
        return {'hello': 'world'}

if __name__ == "__main__": 
    uvicorn.run(app, port=5000, debug=True)