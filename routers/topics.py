from fastapi import APIRouter, Depends, HTTPException
from Models.topicModels import Topics
from Schemas.topicSchemas import TopicCreate, TopicResponse
from sqlalchemy.orm import Session
from database import get_db
from Models.userModel import User
from utility.security import get_admin
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

@router.delete("/topic/{id}")
def delete_topic(id:int,db:Session=Depends(get_db),current_admin:User=Depends(get_admin)):
     topic = db.query(Topics).filter(Topics.id == id).first()
     if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
     return topic
