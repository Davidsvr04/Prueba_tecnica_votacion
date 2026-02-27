from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.voter import Voter
from app.models.candidate import Candidate
from app.schemas.voterSchema import VoterCreate


def create_voter(db: Session, voter_data: VoterCreate):

    existing_voter = db.query(Voter).filter(
        Voter.email == voter_data.email
    ).first()

    if existing_voter:
        raise HTTPException(status_code=400, detail="Email already registered")

    existing_candidate = db.query(Candidate).filter(
        Candidate.cedula == voter_data.cedula
    ).first()

    if existing_candidate:
        raise HTTPException(status_code=400, detail="Esta persona ya esta registrada")

    new_voter = Voter(
        name=voter_data.name,
        email=voter_data.email,
        cedula=voter_data.cedula
    )

    db.add(new_voter)
    db.commit()
    db.refresh(new_voter)

    return new_voter


def get_all_voters(db: Session):
    return db.query(Voter).all()


def get_voter_by_id(db: Session, voter_id: int):
    voter = db.query(Voter).filter(Voter.id == voter_id).first()

    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")

    return voter


def delete_voter(db: Session, voter_id: int):
    voter = db.query(Voter).filter(Voter.id == voter_id).first()

    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")

    db.delete(voter)
    db.commit()

    return {"message": "Voter deleted successfully"}