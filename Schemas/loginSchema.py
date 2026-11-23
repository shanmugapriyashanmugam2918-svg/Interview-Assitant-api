from pydantic import BaseModel

class UserLogin(BaseModel):
    email:str
    pwd:str

class Token(BaseModel):
    access_token:str
    token_type:str