from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.database.base import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)

    voter_id = Column(
        Integer,
        ForeignKey("voters.id", ondelete="CASCADE"),
        nullable=False
    )

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id", ondelete="CASCADE"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint("voter_id", name="unique_vote"),
    )