from fastapi import APIRouter , HTTPException
from schemas import Answer
from data import  answer_history


router=APIRouter()
@router.post("/answer", status_code=201)
def submit_answer(answer: Answer):
    answer_history.append(answer.model_dump())
    return {"status": "Received", "topic": answer.topic}


@router.get("/history", response_model=list[Answer])
def gethistory():
    return answer_history