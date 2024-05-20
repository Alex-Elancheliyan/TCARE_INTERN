from pydantic import BaseModel, EmailStr

class NewUser(BaseModel):
    name:str
    age :int
    emailid:EmailStr


user = NewUser(name= "Alex",age=26, emailid="alex.cheliyan@gmail.com")
print(user.name)
print(user.age)
print(user.emailid)


wrong_data =NewUser(name="Alex",age=25,emailid="alex.cheyangmail.com")
print(wrong_data.name)
print(wrong_data.age)
print(wrong_data.emailid)