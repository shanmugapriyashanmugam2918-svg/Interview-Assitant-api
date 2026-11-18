from pydantic import BaseModel
from typing import Optional


class QuestionCreate(BaseModel):
    question: str
    topic_name: str


class QuestionResponse(BaseModel):
    id: int
    question: str
    answers: list[AnswerResponse] = []
    topic_name: Optional[str]
    model_config = {"from_attributes": True}

class QuestionTopicResponse(BaseModel):
    id: int
    question: str
    model_config = {"from_attributes": True}

class Answercreate(BaseModel):
    answer: str
    question_id: int


class AnswerResponse(BaseModel):
    id: int
    answer_text: str
    question_id: int
    model_config = {"from_attributes": True}

class TopicCreate(BaseModel):
    topic_name: str


class TopicResponse(BaseModel):
    id: int
    topic_name: str
    questions: list[QuestionTopicResponse] = []
    model_config = {"from_attributes": True}