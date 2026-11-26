from pydantic import BaseModel
from typing import Optional
from Schemas.questionSchema import QuestionTopicResponse


class TopicCreate(BaseModel):
    topic_name: str


class TopicResponse(BaseModel):
    id: int
    topic_name: str
    questions: list[QuestionTopicResponse] = []
    model_config = {"from_attributes": True}
