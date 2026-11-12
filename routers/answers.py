from fastapi import APIRouter, HTTPException, Depends
from schemas import Answercreate
from models import Answers, Question
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.get("/answer")
def get_ans(db: Session = Depends(get_db)):
    answers = db.query(Answers).all()
    return answers


@router.post("/answer")
def submit_answer(ans: Answercreate, db: Session = Depends(get_db)):
    question_check = db.query(Question).filter(Question.id == ans.question_id).first()
    if question_check is None:
        raise HTTPException(status_code=404, detail="question not found")
    new_answer = Answers(answer_text=ans.answer, question_id=ans.question_id)
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return {"status": "Received", "answer": new_answer.answer_text}
