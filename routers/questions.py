from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Models.topicModels import Topics
from Models.questionModels import Question
from Schemas.questionSchema import QuestionCreate, QuestionResponse
from database import get_db

router = APIRouter()


@router.get("/questions")
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions


@router.get("/questions/{id}", response_model=QuestionResponse)
def get_questions(id: int, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.id == id).first()
    if questions is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return questions


@router.post("/questions")
def create_questions(ques: QuestionCreate, db: Session = Depends(get_db)):
    topic = db.query(Topics).filter(Topics.topic_name == ques.topic_name).first()
    if topic is None:
        topic = Topics(topic_name=ques.topic_name)
        db.add(topic)
        db.flush()
    new_question = Question(question=ques.question, topic=topic)
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
    topic = (
        db.query(Topics).filter(Topics.topic_name == updated_ques.topic_name).first()
    )
    if topic is None:
        topic = Topics(topic_name=updated_ques.topic_name)
        db.add(topic)
    questions.question = updated_ques.question
    questions.topic = topic
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
