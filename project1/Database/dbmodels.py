
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .MSDatabase import Base


class Users(Base):
    __tablename__ = "usersdata"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, unique=True, index=True)