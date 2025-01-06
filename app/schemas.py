from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = False

    """class Config:
        orm_mode = True"""

class CreatePostRequest(PostBase):
    owner_id: int


class UpdatePostRequest(CreatePostRequest):
    ...


class CreatePostResponse(PostBase):
    owner_id: int
    created_at: datetime


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    """class Config:
        orm_mode = True"""
        


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str


class CreateUserResponse(BaseModel):
    id: int
    email: EmailStr
       

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str    


class TokenData(BaseModel):
    id: Optional[int]


class Vote(BaseModel):
    post_id: int
    dir: int
    
    


