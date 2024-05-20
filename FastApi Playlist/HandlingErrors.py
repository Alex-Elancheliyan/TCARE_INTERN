from fastapi import FastAPI, HTTPException,Request,status
from pydantic import BaseModel
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder

app= FastAPI()

items ={ "Hello":"Welcome Come TCare"}

@app.get("/items/{item_id}")
async def read_item(item_id:str):
    if item_id not in items:
        raise HTTPException (status_code=404,
                             detail="Item Not Found",
                             headers={"X-Error":"The Error Occured"})
    return {"items":items[item_id]}

class UnicornException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request:Request, exc:UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message":f"Oops! {exc.name} did something Wrong"},
    )

@app.get("/unicorns/{name}")
async def read_unicorns(name:str):
    if name== "Alex":
        raise UnicornException(name=name)
    return {"unicorn_name":name}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc),status_code=400)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail),status_code=exc.status_code)

@app.get("/validation_items/{item_id}")
async def read_validation_items(item_id:int):
    if item_id ==3:
        raise HTTPException(status_code=418,detail="3 is not Found")
    return {"item_id":item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request, exc:RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"details":exc.errors(),"body":exc.body}),

    )

class Item(BaseModel):
    title:str
    size:int

@app.post("/items/")
async def create_item(item:Item):
    return item