from fastapi import FastAPI, Depends,Body,Header,HTTPException
import uvicorn


#app= FastAPI(dependencies=[Depends(verify_token),Depends(verify-key)])
'''
#Common Functionality for Dependency
async def common_parameter(q:str | None=None, skip:int=0,limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}

@app.get("/items/")
async  def read_items(commons:dict=Depends(common_parameter)):
    return commons

@app.get("/users/")
async def read_users(commons:dict=Depends(common_parameter)):
    print(commons)
    return commons
'''
#CLASSES AS DEPENDENCIES
'''
fake_items_db = [{"items_name":"Foo"},{"item_name":"bar"},{"item_name":"baz"}]

class CommonQueryParams:
    def __init__(self,q:str | None = None,skip:int=0,limit:int=100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons:CommonQueryParams=Depends(CommonQueryParams)):
    response ={}
    if commons.q:
        response.update({"q":commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items":items})
    return response
'''
#SUB-DEPENDENCIES (Dependency Depending on another Dependency)
'''
def get_query(q:str| None=None):
    return q

def query_or_body_extractor(
        q:str = Depends(get_query),last_query:str |None=Body (None)
):
    if q:
        return q
    return last_query

@app.post("/item")
async def try_query(get_query:str = Depends(query_or_body_extractor)):
    return {"get_query":get_query}

'''

#Dependency In Path Operation Decorators:

async def verify_token(x_token:str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=400,detail="X-Token Header Invalid")

async def verify_key(x_key:str = Header(...)):
    if x_key !="secret-key":
        raise HTTPException(status_code=400,detail="X-Key Header Invalid")
    return x_key

app= FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])

@app.get("/items")
async def read_items():
    return[{"item":"Pepsi"},{"items":"Cola"}]

@app.get("/users")
async def get_user():
    return[{"username":"Alex","Position":"Software Intern"}]









if __name__ == '__main__':
    uvicorn.run("Dependencies:app", host="127.0.0.1", port=8000,reload=True)