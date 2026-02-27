from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.candidate import Candidate
from app.models.voter import Voter
from app.schemas.candidateSchema import CandidateCreate


def create_candidate(db: Session, candidate_data: CandidateCreate):

    existing_voter = db.query(Voter).filter(
        Voter.cedula == candidate_data.cedula
    ).first()

    if existing_voter:
        raise HTTPException(status_code=400, detail="Esta persona ya esta registrada")

    new_candidate = Candidate(
        name=candidate_data.name,
        cedula=candidate_data.cedula,
        party=candidate_data.party
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate


def get_all_candidates(db: Session, skip: int = 0, limit: int = 10, name: str = None, party: str = None):
    query = db.query(Candidate)
    
    if name:
        query = query.filter(Candidate.name.ilike(f"%{name}%"))
    
    if party:
        query = query.filter(Candidate.party.ilike(f"%{party}%"))
    
    return query.offset(skip).limit(limit).all()


def get_candidate_by_id(db: Session, candidate_id: int):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    return candidate


def delete_candidate(db: Session, candidate_id: int):
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    db.delete(candidate)
    db.commit()

    return {"message": "Candidato eliminado exitosamente"}