import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta

# SECRET KEY
# ALGORITHM
# ACCESS_TOKEN_EXPIRY_MINUTES

SECRET_KEY = "28h49r4024hf248hf0g84t79gygrfhbnrweiqujh0q83390u2qhn0821jsq"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    # provided a copy of data to work on without changing the actual data
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # added extra information by adding to the existing data
    to_encode.update({"exp": expiry})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


