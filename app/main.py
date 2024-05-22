from fastapi import FastAPI
import psycopg2

from . import models, schemas,utils
from .database import get_db,engine
from .routers import post, user, auth


# will create all the corresponding tables in the database based on models defined in model.py .
models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)






"""
from pydantic import ValidationError

try:
    ...
    
except ValidationError as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))"""
