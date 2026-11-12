from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from routers.questions import router as questions_router
from routers.answers import router as answers_router
from database import engine, Base, get_db


Base.metadata.create_all(bind=engine)
app = FastAPI()
# app.include_router(topics_router)
app.include_router(answers_router)
app.include_router(questions_router)


