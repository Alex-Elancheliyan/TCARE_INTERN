from fastapi import FastAPI

app = FastAPI()

@app.post("/items/",status_code=201)
async def create_item(name:str):
    return {"name":name}


@app.delete("/items/{pk}",status_code=204)
async def delete_items(pk:str):
    print("pk",pk)
    return pk

@app.get("/items/",status_code=301)
async def read_items_redirect():
    return {"hello":"world"}
