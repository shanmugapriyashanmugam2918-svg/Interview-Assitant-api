from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    topic = Column(String)
    answers = relationship("Answers", back_populates="question")

class Answers(Base):
    __tablename__="answers"
    id = Column(Integer, primary_key=True)
    answer_text = Column(String)
    question_id=Column(Integer,ForeignKey("questions.id"))
    question = relationship("Question", back_populates="answers")
