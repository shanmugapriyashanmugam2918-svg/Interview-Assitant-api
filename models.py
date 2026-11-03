from sqlalchemy import Column, Integer, String
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    topic = Column(String)
