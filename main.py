from fastapi import FastAPI
from models import Topic
from data import topics, questions

app = FastAPI()


# get endpoint for root, topics, and search
@app.get("/")
def root():
    return {"message": "Welcome to the Interview Assistant API"}


@app.get("/topics")
def get_topics():
    return {"topics": topics}


@app.get("/topics/{topic_id}")
def get_topics(topic_id: int):
    return topics[topic_id]


@app.get("/search")
def search(topic: str):
    return f"you have searched for topic: {topic}"


# Post endpoint for candidate


@app.post("/topics")
def add_topic(topic: Topic):
    topics.append(topic)
    return {"message": "Topic added successfully", "topics": topics}


# PUT endpoint


@app.put("/topics/{topic_id}")
def update_topics(topic_id: int, topic: Topic):
    topics[topic_id] = topic
    return {"message": "Topic updated successfully", "topics": topics}


# Delete endpoint


@app.delete("/topics/{topic_id}")
def delete_topic(topic_id: int):
    if 0 <= topic_id < len(topics):
        deleted_topic = topics.pop(topic_id)
        return {"message": "Topic deleted successfully", "topics": deleted_topic}
    return {"message": "Topic not found"}
