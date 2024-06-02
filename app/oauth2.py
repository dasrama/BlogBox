import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError, PyJWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from .schemas import Token, TokenData
from . import schemas, database, models


oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET KEY
# ALGORITHM
# ACCESS_TOKEN_EXPIRY_MINUTES

SECRET_KEY = "28h49r4024hf248hf0g84t79gygrfhbnrweiqujh0q83390u2qhn0821jsq"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict) -> Token:
    # provided a copy of data to work on without changing the actual data
    to_encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # added extra information by adding to the existing data
    to_encode.update({"exp": expiry})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credential_exception) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if not id:
            raise credential_exception

        token_data = TokenData(id=id) 
        return token_data
    except PyJWTError:
        raise credential_exception
    
    
def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credential_exception)
    current_user = db.query(models.User).filter(models.User.id == token.id).first()

    return current_user
