#IMPORTING MODULES

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.orm import declarative_base

#ENGINE CREATION
DB_URL ='postgresql://postgres:your db credentials here'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()



