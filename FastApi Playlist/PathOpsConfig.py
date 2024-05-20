from fastapi import FastAPI, HTTPException,Request,status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str| None=None
    price:float
    tax:float|None=None
    tags:set[str]=set()

class Tags(Enum):
    items="item"
    user="user"

@app.post("/items/",response_model=Item,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.items],)
          #summary="Create an Item",
          #description="Create an Item with all information like Name, Description,Price,Tax,Tags")
async def create_items(item:Item):
    """
     Create an Item with all the Information:
    - **name**: Each Item Must Have a Name.
    - **description**: A long Description.
    - **price**: Price is Required.
    - **tax**: If the Item doesn't have tax, we can Omit it.
    - **tags**: A set of unique tag strings for this Item.
    """
    return item

@app.get("/items/",tags=[Tags.items])
async def read_items():
    return[{"name":"Pepsi","Price":42}]

@app.get("/users/",tags=[Tags.user],deprecated=True)
async def read_user():
    return [{"username":"Alex"}]
