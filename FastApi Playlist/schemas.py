from pydantic import BaseModel

class Address(BaseModel):
    addline1:str
    addline2:str
    city:str
    state:str
    zip_codes:str

class CreateList(BaseModel):
    id: int
    name:str
    contact:str
    alternate_contact:str
    email: str
    address: Address

