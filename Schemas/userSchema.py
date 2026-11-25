from pydantic import BaseModel, ConfigDict


class userCreate(BaseModel):
    username: str
    email: str
    password: str


class userResponse(BaseModel):
    id: int
    username: str
    email: str
    role:str
    model_config = ConfigDict(from_attributes=True)
    
