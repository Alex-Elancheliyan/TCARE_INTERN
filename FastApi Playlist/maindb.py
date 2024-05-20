from fastapi import FastAPI , Depends ,HTTPException
from schemas import CreateList,Address
from sqlalchemy.orm import Session
from database import get_db
from models import UserData

app = FastAPI()

@app.post("/user/create")
def create (details:CreateList,db:Session=Depends(get_db)):
    to_create = UserData(
        id=details.id,
        name = details.name,
        contact=details.contact,
        alternate_contact=details.alternate_contact,
        email=details.email,
        addline1=details.address.addline1,
        addline2=details.address.addline2,
        city=details.address.city,
        state=details.address.state,
        zip_code=details.address.zip_codes
    )
    db.add(to_create)
    db.commit()
    return {'Success':True,"created_id": to_create.id}

@app.delete("/")
def delete(id=int,db:Session= Depends(get_db)):
    db.query(UserData).filter(UserData.id==id).delete()
    db.commit()
    return {"Deletion Successful":id}

@app.get("/all_data")
def all_data (db: Session = Depends(get_db)):
    users = db.query(UserData).all()
    return users

@app.put("/update")
def update(id: int, details: CreateList, db: Session = Depends(get_db)):
    detail = db.query(UserData).filter(UserData.id == id).first()
    if not detail:
        raise HTTPException(status_code=404, detail="details not found")
    detail.name = details.name,
    detail.contact = details.contact,
    detail.alternate_contact = details.alternate_contact,
    detail.email = details.email,
    detail.addline1 = details.address.addline1,
    detail.addline2 = details.address.addline2,
    detail.city = details.address.city,
    detail.state = details.address.state,
    detail.zip_code = details.address.zip_codes
    db.commit()
    return {"Details Updated At ID No":id}









