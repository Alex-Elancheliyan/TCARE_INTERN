from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from datetime import datetime
from fastapi.encoders import jsonable_encoder


app=FastAPI()


class Item(BaseModel):
    name:str |None=None
    description:str |None=None
    price:float |None=None
    tax:float=10.5
    tags:list[str]=[]

items ={
    "item1":{"name":"Pepsi","price":50.2},
    "item2":{"name":"Coke","description":"Nice Drink","price":35,"tax":12.4},
    "item3":{"name":"Fanta","description":None,"price":35.00,"tax":12.5,"tags":[]},

}

@app.get("/items/{item_id}",response_model=Item)
async def read_item(item_id:str):
    return items.get(item_id)

@app.put("/items/{item_id}",response_model=Item)
def update_item(item_id:str, item:Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id]=update_item_encoded
    return update_item_encoded

@app.patch("/items/{item_id}",response_model=Item)
def patch_item(item_id:str, item:Item):
    stored_item_data = items.get(item_id)
    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model=Item()
    update_data= item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id]=jsonable_encoder(updated_item)
    print(items[item_id])
    return updated_item

if __name__ == '__main__':
    uvicorn.run("JsonEncoder:app", host="127.0.0.1", port=8000,reload=True)

