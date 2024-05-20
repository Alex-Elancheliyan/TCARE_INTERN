from sqlalchemy import Column, String, Integer
from database import Base
#SAMPLE MODEL FOR CREATING A TABLE
class UserData(Base):
    __tablename__ = "details"
    id = Column(Integer, primary_key= True)
    name = Column(String,nullable=True)
    contact = Column (String,nullable=False)
    alternate_contact= Column(String, nullable=False)
    email = Column(String,nullable=False)
    addline1= Column(String,nullable=False)
    addline2= Column(String,nullable=False)
    city= Column(String,nullable=False)
    state= Column(String,nullable=False)
    zip_code= Column(String,nullable=False)

