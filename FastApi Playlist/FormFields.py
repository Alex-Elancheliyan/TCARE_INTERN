
from fastapi import FastAPI,Form
from pydantic import BaseModel

app=FastAPI()


@app.post("/login/")
async def login_data(username:str=Form(...),password:str=Form(...)):
    return {"username":username}

class User(BaseModel):
    username:str
    password:str

@app.post("/login_json/")
async def login_json(user:User):
    return user

