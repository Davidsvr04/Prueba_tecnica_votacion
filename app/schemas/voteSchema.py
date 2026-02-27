from pydantic import BaseModel

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteResponse(BaseModel):
    id: int
    voter_id: int
    candidate_id: int

    class Config:
        from_attributes = True