from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Question
from schemas import QuestionCreate
from database import get_db

router = APIRouter()


@router.get("/questions")
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions


@router.get("/questions/{id}")
def get_questions(id: int, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.id == id).first()
    return questions


@router.post("/questions")
def create_questions(ques: QuestionCreate, db: Session = Depends(get_db)):
    new_question = Question(question=ques.question, topic=ques.topic)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


@router.put("/questions/{id}")
def update_questions(
    id: int, updated_ques: QuestionCreate, db: Session = Depends(get_db)
):
    questions = db.query(Question).filter(Question.id == id).first()
    if questions is None:
        raise HTTPException(status_code=404, detail="Question not found")
    questions.question = updated_ques.question
    db.commit()
    db.refresh(questions)
    return questions


@router.delete("/questions/{id}")
def delete_questions(id: int, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.id == id).first()
    if questions is None:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(questions)
    db.commit()
    return {"message": "Question deleted "}
