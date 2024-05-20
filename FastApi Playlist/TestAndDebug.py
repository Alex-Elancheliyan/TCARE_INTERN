#Testing:
from fastapi import FastAPI, HTTPException,Header,status
from pydantic import BaseModel

app=FastAPI()

fake_secret_token = "coneofsilence"

fake_db = dict(
    foo=dict(
        id="foo",title="Foo",description="There Goes My Hero",
    ),
    bar=dict(
        id="bar",title="Bar",description="The bartenders",
    ),
)

class Item(BaseModel):
    id:str
    title:str
    description:str | None=None

@app.get("/items/{item_id}",response_model=Item)
async def read_main(item_id:str,x_token:str= Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400,detail="Invalid X-Token Header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="item not found")
    return fake_db[item_id]

@app.post("/items/",response_model=Item)
async def create_item(item:Item,x_token:str=Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400,detail="Invalid X-Token Header")
    if item.id in fake_db:
        raise HTTPException(status_code=404,detail="item already exists")
    fake_db[item.id]=item
    return item




