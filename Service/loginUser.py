from Models.userModel import User
from utility import security
from fastapi import HTTPException


def login_user(db, login_data):
    user_check = db.query(User).filter(User.email == login_data.email).first()
    if user_check is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    is_valid=security.verify_pwd(login_data.pwd,user_check.password)
    if not is_valid:
         raise HTTPException(status_code=401, detail="Invalid credentials")
    token = security.create_access_token({"sub":user_check.email})
    return{
        "access_token":token,
        "token_type":"bearer"
    }


