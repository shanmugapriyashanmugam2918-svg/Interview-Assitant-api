from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = "usersList"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password= Column(String, unique=True, nullable=False)
    role=Column(String,default="user")