#IMPORTING MODULES

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.orm import declarative_base




#ENGINE CREATION
DB_URL ='postgresql URL credentials'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

#Base.metadata.create_all(bind=engine) --> #We can use this code if we wanted to create table without using the alembic.

#TO GET A SESSION TO USE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


