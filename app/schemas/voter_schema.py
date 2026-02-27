from pydantic import BaseModel, EmailStr

class VoterCreate(BaseModel):
    name: str
    email: EmailStr

class VoterResponse(BaseModel):
    id: int
    name: str
    email: str
    has_voted: bool

    class Config:
        from_attributes = True