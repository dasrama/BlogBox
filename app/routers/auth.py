from fastapi import Depends, APIRouter, Response, HTTPException, status
from .. import database, schemas
from sqlalchemy.orm import Session
from .. import models, utils


router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(user_credentials : schemas.UserLogin, db : Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
     
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "invalid user credentials")
    
    # print(user)
    
    if not utils.verify(plain_password= user_credentials.password,hashed_password= user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")

    # create a token
    # return token
    return {"token" : "example"}
    
