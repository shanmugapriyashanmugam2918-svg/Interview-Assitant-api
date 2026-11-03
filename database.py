from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = URL.create(
    "postgresql+psycopg",
    username="postgres",  # Use the username shown in pgAdmin
    password="*****",
    host="localhost",
    port=5432,
    database="interview_assitant",
)

# Connection
engine = create_engine(DATABASE_URL)

# database sessions

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# parentclass for all models
Base = declarative_base()
