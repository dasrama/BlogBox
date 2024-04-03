from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # created_at : datetime

    """class Config:
        orm_mode = True"""

class CreatePostRequest(BaseModel):
    title: str
    content: str


class UpdatePostRequest(CreatePostRequest):
    ...


class CreatePostResponse(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at : datetime


class GetPostResponse(CreatePostRequest):
    ...

    

    


