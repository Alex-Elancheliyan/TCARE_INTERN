from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str | None=None
    price:float
    tax:float |None = None

class User(BaseModel):
    username:str
    full_name:str | None=None

class Importance(BaseModel):
    importance:int

@app.put("/items/{item_id")
async def update_item(
        *,
        item_id: int = Path(...,title="The ID of the item to Get",ge=0,le=150),
        q: str | None=None,
        item:Item | None=None,
        user:User,
        importance : Importance
):
        results={"Item_ID":item_id}
        if q:
            results.update({"q":q})
        if item:
            results.update({"Items":item})
        if user:
            results.update({"User":user})
        if importance:
            results.update({"Importance": importance})
        return results