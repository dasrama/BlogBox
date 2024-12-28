from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #JWT
    SECRET_KEY : str = "28h49r4024hf248hf0g84t79gygrfhbnrweiqujh0q83390u2qhn0821jsq"
    ALGORITHM : str= "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60

    #DATABASE
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str

    class Config:
        env_file = ".env"

