from fastapi import FastAPI,Body
from pydantic import BaseModel,Field


app= FastAPI()
class Item(BaseModel):
   name: str
   description: str|None = None
   price: float
   tax: float | None=None


@app.put("/items/{item_id}")
async def update_item(
       item_id:int,
       item:Item=Body(
           ...,
           example={"name":"Pepsi",
                    "description":"Very Good Drink",
                    "price":25.00,
                    "tax":1.5})):
   results ={"Item Id ":item_id,"item":item}
   return results