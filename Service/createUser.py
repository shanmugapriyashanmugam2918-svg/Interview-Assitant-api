from Models.userModel import User
from utility import security
from fastapi import HTTPException


def register_user(db, user):
    username_check = db.query(User).filter(User.username == user.username).first()
    email_check = db.query(User).filter(User.email == user.email).first()
    if username_check is not None:
        raise HTTPException(status_code=400, detail="username already exist")
    if email_check is not None:
        raise HTTPException(status_code=400, detail="Email already exist")

    hashed_pwd = security.hash_pwd(user.password)
    newUser = User(username=user.username, email=user.email, password=hashed_pwd,role="user")
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
