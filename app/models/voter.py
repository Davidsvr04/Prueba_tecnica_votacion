from sqlalchemy import Column, Integer, String, Boolean
from app.database.base import Base

class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    cedula = Column(String(20), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    has_voted = Column(Boolean, default=False)