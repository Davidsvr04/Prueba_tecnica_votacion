from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    cedula: str
    party: str | None = None

class CandidateResponse(BaseModel):
    id: int
    name: str
    cedula: str
    party: str | None
    votes: int

    class Config:
        from_attributes = True