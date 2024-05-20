#IMPORTING MODULES
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#CREATING  DB URL
DB_URL ='postgresql://postgres:1234@localhost/AlexDataBase'

#ENGINE CREATION
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#FUNC TO RETRIVE A DB SESSION.
#WE CAN IMPORT FUNC IN OTHER FILES LATER TO GET A SESSION TO USE
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()