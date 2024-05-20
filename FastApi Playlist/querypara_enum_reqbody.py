from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/")
async def get_root():
    return {"message": "Hello World"}

@app.get("/name")
async def username():
    return{"message":"route for name"}

@app.get("/name/{user_name}")
async def get_user_name(user_name):
    return {"Name of the User": user_name}

@app.get("/name/{user_name}/userid/{user_id}")
async def get_userid(user_name: str ,user_id: int):
    return({"Name of the user":user_name,"User Id is": user_id})

#ENUM
class Partnership(int,Enum):
    opening = 100
    middleorder = 30
    finishers = 80

@app.get("/partnership/{runs_scored}")
async def team_score(runs_scored:Partnership):
    if runs_scored == Partnership.opening:
        return{"Runs Scored":runs_scored,"message":"Winning Chance is High"}
    if runs_scored.middleorder == 30:
        return{"Runs Scored":runs_scored,"message":"Winning Chance is Low"}


#QUERY PARAMETER

@app.get("/items/{item_id}")
async def get_itemid(item_id: str,q:str|None=None,short:bool =False):
    items={"item_id":item_id}
    if q:
        items.update({"q":q})
    if not short:
        items.update({"description":" TCARE description is added"})
    return items

#HANDLING REQUEST BODY

class Playername():
    name : str
    runs : int
players=[]
@app.post("/players/")
async def player_name(players:Playername):
    players.append(Playername)
    return{"Player Name":players, "Message":"Playername Added!" }

