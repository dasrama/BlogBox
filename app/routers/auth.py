from fastapi import Depends, APIRouter, Response
from .. import database
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
def login(db : Session= Depends(database.get_db)):
    ...