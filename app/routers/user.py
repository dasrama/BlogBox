from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from ..utils import hash 


router = APIRouter(
    tags=["User"]
)




@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateUserResponse)
def create_user(user: schemas.CreateUserRequest, db: Session = Depends(get_db)):
    # print(user.password)
    # hash the password - user.password
    hashedPassword = utils.hash(user.password)
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