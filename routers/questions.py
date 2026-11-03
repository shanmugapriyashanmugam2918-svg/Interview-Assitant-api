from fastapi import APIRouter , HTTPException
from data import  topics,questions
import random

router=APIRouter()
@router.get("/questions")
def get_questions(topic: str):
    print("Topic is:", topics)
    print("questions:", questions)
    filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
    if not filtered_questions:
        raise HTTPException(
            status_code=404,
            detail=f"No questions found for topic {topic}",
        )
    return random.choice(filtered_questions)