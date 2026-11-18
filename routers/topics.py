from fastapi import APIRouter, Depends, HTTPException
from models import Topics
from schemas import TopicCreate, TopicResponse
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.get("/topics")
def get_topics(db: Session = Depends(get_db)):
    topics = db.query(Topics).all()
    return topics


@router.get("/topics/{topic_id}", response_model=TopicResponse)
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topics).filter(Topics.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic

