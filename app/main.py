from fastapi import FastAPI
from app import models
from app.database import engine

from app.routers.auth import router as AuthBackend
from app.routers.post import router as PostRouter
from app.routers.user import router as UserRouter


# will create all the corresponding tables in the database based on models defined in model.py .
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(AuthBackend, tags=["Authentication"])
app.include_router(PostRouter, tags=["Post"], prefix="/post")
app.include_router(UserRouter, tags=["User"], prefix="/user")

