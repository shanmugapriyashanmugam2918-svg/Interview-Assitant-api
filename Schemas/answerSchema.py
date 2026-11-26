from pydantic import BaseModel
from typing import Optional


class Answercreate(BaseModel):
    answer: str
    question_id: int


class AnswerResponse(BaseModel):
    id: int
    answer_text: str
    question_id: int
    model_config = {"from_attributes": True}
