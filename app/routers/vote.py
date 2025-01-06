from fastapi import FastAPI, APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.oauth2 import get_current_user
from app.schemas import Vote
from app.models import Vote as VoteModel

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: Vote, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    vote_query = db.query(VoteModel).filter(VoteModel.post_id==vote.post_id, VoteModel.user_id==current_user)
    found_vote = vote_query.first()
    print(" ")
    print("found_vote: ", found_vote)
    print(" ")

    if vote.dir==0:
        ...
    else:
        ...    

    return dict()