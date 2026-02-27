from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    party = Column(String(100), nullable=True)
    votes = Column(Integer, default=0, nullable=False)