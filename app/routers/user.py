from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from ..utils import hash 


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateUserResponse)
def create_user(user: schemas.CreateUserRequest, db: Session = Depends(get_db)):
    hashedPassword = utils.hash(user.password)
    user.password = hashedPassword

    new_user = models.User(**user.dict())
    query = db.query(models.User.email).filter(models.User.email == user.email)
    existing_user = query.first()
    if existing_user != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="email already registered")
    
    # **user.dict() unpacks the dictionary user into keyword arguments and pass it into the fields of User model defined in models.py
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user