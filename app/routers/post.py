from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(tags=["Post"])

@router.get("/posts", response_description="Get Posts", response_model = list[schemas.GetPostResponse])
def get_posts(db: Session = Depends(get_db), current_id = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    # print(type(posts))
    # type : list having Post as elements
    return posts


@router.post("/posts", response_description="Create Post", status_code=status.HTTP_201_CREATED, response_model=schemas.CreatePostResponse)
def create_posts(post: schemas.Post, db: Session=Depends(get_db), current_id = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict())
    # print(type(current_id))   -> int
    # **post.dict() unpacks the dictionary post into keyword arguments
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # print(type(posts))
    return new_post


@router.get("/posts/{id}", response_description="Get Anyone Post", response_model=schemas.GetPostResponse)
def get_post(id, db: Session = Depends(get_db), current_id = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post


@router.delete("/posts/{id}", response_description="Delete post", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id, db: Session = Depends(get_db), current_id = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}", response_description="Update Post")
def update_post(id, update_post: schemas.Post, db: Session = Depends(get_db), current_id = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return {"msg":"successfully updated the post"}


