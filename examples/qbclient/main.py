from logging import debug
from qbodbc import QB 
from fastapi import FastAPI, Body
from Pyda
import uvicorn 

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
def root(): 
    return "Hello World!"

@app.post("/customer/customers")
def customer_create(data, item): 
    # print(data)
    breakpoint()
    # con = QB()
    return "Hello"

if __name__ == "__main__": 
    uvicorn.run(app, debug=True)