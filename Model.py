from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    # ... all columns for the User table ...

class Story(Base):
    __tablename__ = "stories"
    # ... all columns for the Story table ...
