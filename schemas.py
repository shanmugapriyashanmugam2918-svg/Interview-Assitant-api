from pydantic import BaseModel


class QuestionCreate(BaseModel):
    question: str
    topic: str


class QuestionResponse(BaseModel):
    id: int
    question: str
    answers: list[AnswerResponse] = []
    topic: str
    model_config = {"from_attributes": True}


class Answercreate(BaseModel):
    answer: str
    question_id: int


class AnswerResponse(BaseModel):
    id: int
    answer_text: str
    question_id: int
    model_config = {"from_attributes": True}
