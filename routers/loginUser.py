from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from Schemas.loginSchema import UserLogin
from Service import loginUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/login")
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):

    return loginUser.login_user(db, login_data)
