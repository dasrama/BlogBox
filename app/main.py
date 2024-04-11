from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db,engine
import psycopg2
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
# here we are specifying the algorithm used for hashing : i.e bcrypt

# will create all the corresponding tables in the database based on models defined in model.py .
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/posts", response_model = list[schemas.GetPostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # print(type(posts))
    # type : list having Post as elements
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED,response_model=schemas.CreatePostResponse)
def create_posts(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    # **post.dict() unpacks the dictionary post into keyword arguments
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # print(type(posts))
    return new_post


@app.get("/posts/{id}",response_model = schemas.GetPostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    # print(type(post))
    return post.first()


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, update_post: schemas.Post, db: Session = Depends(get_db)):


    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.update(update_post.dict(), synchronize_session=False)

    db.commit()

    return {"msg":"successfully updated the post"}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateUserResponse)
def create_user(user: schemas.CreateUserRequest, db: Session = Depends(get_db)):
    # print(user.password)
    # hash the password - user.password
    hashedPassword = pwd_context.hash(user.password)
    user.password = hashedPassword

    new_user = models.User(**user.dict())
    #print(user.email)
    query = db.query(models.User.email).filter(models.User.email == user.email)
    #print(query)
    existing_user = query.first()
    if existing_user != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="email already registered")
    
    # **user.dict() unpacks the dictionary user into keyword arguments and pass it into the fields of User model defined in models.py
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    #print(type(new_user))
    return new_user



"""
from pydantic import ValidationError

try:
    ...
    
except ValidationError as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))"""
