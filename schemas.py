from pydantic import BaseModel

class Topic(BaseModel):
    id:int
    name:str

class Answer(BaseModel):
    topic:str
    question:str
    answer:str

class QuestionCreate(BaseModel):
    question:str
    topic:str