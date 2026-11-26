from pydantic import BaseModel
from typing import Optional
from Schemas.answerSchema import AnswerResponse

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