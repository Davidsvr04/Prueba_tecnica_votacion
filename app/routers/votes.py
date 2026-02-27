from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.voteSchema import VoteCreate, VoteResponse
from app.schemas.userSchema import UserResponse
from app.services import votingService
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/votes", tags=["Votes"])


@router.post("/", response_model=VoteResponse)
def create_vote(
    vote: VoteCreate, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    return votingService.create_vote(db, vote)


@router.get("/", response_model=list[VoteResponse])
def get_votes(db: Session = Depends(get_db)):
    return votingService.get_all_votes(db)


@router.get("/statistics")
def get_statistics(db: Session = Depends(get_db)):
    return votingService.get_statistics(db)