from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.voterSchema import VoterCreate, VoterResponse
from app.services import voterService

router = APIRouter(prefix="/voters", tags=["Voters"])


@router.post("/", response_model=VoterResponse)
def create_voter(voter: VoterCreate, db: Session = Depends(get_db)):
    return voterService.create_voter(db, voter)


@router.get("/", response_model=list[VoterResponse])
def get_voters(db: Session = Depends(get_db)):
    return voterService.get_all_voters(db)


@router.get("/{voter_id}", response_model=VoterResponse)
def get_voter(voter_id: int, db: Session = Depends(get_db)):
    return voterService.get_voter_by_id(db, voter_id)


@router.delete("/{voter_id}")
def delete_voter(voter_id: int, db: Session = Depends(get_db)):
    return voterService.delete_voter(db, voter_id)