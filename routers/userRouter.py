from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from Schemas.userSchema import userCreate, userResponse
from Service import createUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=userResponse)
def register_user(user: userCreate, db: Session = Depends(get_db)):
    return createUser.register_user(db, user)
