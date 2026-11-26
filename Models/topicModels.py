from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional
from database import Base



class Topics(Base):
    __tablename__="topics"
    id = Column(Integer, primary_key=True)
    topic_name = Column(String)
    questions = relationship("Question", back_populates="topic")