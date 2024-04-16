
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()




@router.get("/posts", response_model = list[schemas.GetPostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # print(type(posts))
    # type : list having Post as elements
    return posts


@router.post("/posts", status_code=status.HTTP_201_CREATED,response_model=schemas.CreatePostResponse)
def create_posts(post: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    # **post.dict() unpacks the dictionary post into keyword arguments
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # print(type(posts))
    return new_post


@router.get("/posts/{id}",response_model = schemas.GetPostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    # print(type(post))
    return post.first()


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}")
def update_post(id: int, update_post: schemas.Post, db: Session = Depends(get_db)):


    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.update(update_post.dict(), synchronize_session=False)

    db.commit()

    return {"msg":"successfully updated the post"}


