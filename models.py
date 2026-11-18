from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answers = relationship("Answers", back_populates="question")
    topic = relationship("Topics", back_populates="questions")
    topic_id =Column(Integer,ForeignKey("topics.id"))

    @property
    def topic_name(self) -> Optional[str]:
        return self.topic.topic_name if self.topic else None


class Answers(Base):
    __tablename__="answers"
    id = Column(Integer, primary_key=True)
    answer_text = Column(String)
    question_id=Column(Integer,ForeignKey("questions.id"))
    question = relationship("Question", back_populates="answers")

class Topics(Base):
    __tablename__="topics"
    id = Column(Integer, primary_key=True)
    topic_name = Column(String)
    questions = relationship("Question", back_populates="topic")