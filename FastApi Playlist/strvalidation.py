from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/item")

async def get_id(q:str | None= Query(None, min_length=5,max_length=10,title="Beverages",description="List Of Beverages",alias="Bev-Query")):
    results = {"items":[{"item_id":"Milkshake"},{"item_id":"Cool Drinks"}]}
    if q:
        results.update({"Q": q})
    return results

@app.get("/items_hidden")
async def hidden_query_route(hidden_query:str | None=Query(None,include_in_schema=False)):
    if hidden_query:
        return {"Hidden_Query":hidden_query}
    return {"Hidden_Query":"Not Found"}