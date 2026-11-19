from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Models.userModel import User
from Schemas.userSchema import userCreate, userResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=userResponse)
def register_user(user: userCreate, db: Session =Depends(get_db)):
    newUser = User(username=user.username, email=user.email, password=user.password)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
