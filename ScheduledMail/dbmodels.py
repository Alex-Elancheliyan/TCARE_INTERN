
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime 
from sqlalchemy.ext.declarative import declarative_base
from MSDatabase import Base


class Emailreport(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False,unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    name = Column(String, nullable=True)
    title = Column(String, nullable=True)
    organization = Column(String, nullable=True)
    



