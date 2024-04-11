from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
# here we are specifying the algorithm used for hashing : i.e bcrypt

def hash(password : str):
    return pwd_context.hash(password)