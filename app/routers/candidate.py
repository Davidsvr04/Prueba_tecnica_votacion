from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.candidateSchema import CandidateCreate, CandidateResponse
from app.services import candidateService

router = APIRouter(prefix="/candidates", tags=["Candidates"])

@router.post("/", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    return candidateService.create_candidate(db, candidate)


@router.get("/", response_model=list[CandidateResponse])
def get_candidates(skip: int = 0, limit: int = 10, name: str = None, party: str = None, db: Session = Depends(get_db)):
    return candidateService.get_all_candidates(db, skip=skip, limit=limit, name=name, party=party)


@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    return candidateService.get_candidate_by_id(db, candidate_id)


@router.delete("/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    return candidateService.delete_candidate(db, candidate_id)