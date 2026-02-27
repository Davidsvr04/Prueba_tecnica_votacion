from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import func
from app.models.votes import Vote
from app.models.voter import Voter
from app.models.candidate import Candidate
from app.schemas.voteSchema import VoteCreate


def create_vote(db: Session, vote_data: VoteCreate):

    voter = db.query(Voter).filter(Voter.id == vote_data.voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")

    candidate = db.query(Candidate).filter(
        Candidate.id == vote_data.candidate_id
    ).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    if voter.has_voted:
        raise HTTPException(status_code=400, detail="Votante ya ha votado")

    try:
        new_vote = Vote(
            voter_id=vote_data.voter_id,
            candidate_id=vote_data.candidate_id
        )

        voter.has_voted = True
        candidate.votes += 1

        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)

        return new_vote

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al procesar el voto")


def get_all_votes(db: Session):
    return db.query(Vote).all()


def get_statistics(db: Session):

    total_votes = db.query(func.count(Vote.id)).scalar()

    if total_votes == 0:
        return {
            "total_votes": 0,
            "results": [],
            "total_voters_voted": 0
        }

    candidates = db.query(Candidate).all()

    results = []
    for candidate in candidates:
        percentage = (candidate.votes / total_votes) * 100

        results.append({
            "candidate_id": candidate.id,
            "name": candidate.name,
            "total_votes": candidate.votes,
            "percentage": round(percentage, 2)
        })

    total_voters_voted = db.query(func.count(Voter.id)).filter(
        Voter.has_voted == True
    ).scalar()

    return {
        "total_votes": total_votes,
        "results": results,
        "total_voters_voted": total_voters_voted
    }