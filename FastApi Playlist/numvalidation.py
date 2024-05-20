

from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items_validation/{item_id}")
async def read_items(item_id: int=Path(...,title="The ID of the Item To get",gt=10,lt=99),q:str="Hello"):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
