from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from typing import Literal

app = FastAPI()

class Item (BaseModel):
    name:str
    description:str | None=None
    price :float
    tax:float = 10.5
    tags:list[str]=[]

items ={
    "Pepsi": {"name":"Pepsi","price":50.2},
    "Coke":{"name":"Coke","description":"Best Drink","price":50,"tax":10.5},
    "Fanta":{"name":"Fanta","description":None,"price":50.2,"tax":16.3,"tags":[]},
}

@app.post("/item/{item_id}",response_model=Item, response_model_exclude_unset=True)
async def read_items(item_id:Literal["Pepsi","Coke","Fanta"]):
    return items[item_id]

@app.get("/items/{item_id}/name",response_model=Item,response_model_include={"name","price"},tags=["Include"])
async def get_items(item_id : Literal["Pepsi","Coke","Fanta"]):
    return items[item_id]

@app.get("/items/{item_id}/public",response_model=Item,response_model_exclude={"name"})
async def read_items_public(item_id:Literal['Pepsi','Coke','Fanta']):
    return items[item_id]
