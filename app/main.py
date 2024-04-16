from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas,utils
from .database import get_db,engine
import psycopg2
from .routers import post, user




# will create all the corresponding tables in the database based on models defined in model.py .
models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)





"""
from pydantic import ValidationError

try:
    ...
    
except ValidationError as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))"""
