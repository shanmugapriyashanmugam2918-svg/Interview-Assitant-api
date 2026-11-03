from fastapi import APIRouter
from schemas import Topic
from data import topics


router=APIRouter()
@router.get("/topics")
def get_topics():
    return {"topics": topics}
@router.get("/search")
def search(topic: str):
    return f"you have searched for topic: {topic}"
@router.get("/topics/{topic_id}")
def get_topics(topic_id: int):
    return topics[topic_id]

@router.post("/topics")
def add_topic(topic: Topic):
    topics.append(topic)
    return {"message": "Topic added successfully", "topics": topics}

@router.put("/topics/{topic_id}")
def update_topics(topic_id: int, topic: Topic):
    topics[topic_id] = topic
    return {"message": "Topic updated successfully", "topics": topics}

@router.delete("/topics/{topic_id}")
def delete_topic(topic_id: int):
    if 0 <= topic_id < len(topics):
        deleted_topic = topics.pop(topic_id)
        return {"message": "Topic deleted successfully", "topics": deleted_topic}
    return {"message": "Topic not found"}
