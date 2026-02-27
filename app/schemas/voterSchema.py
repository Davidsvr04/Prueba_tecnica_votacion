from pydantic import BaseModel, EmailStr

class VoterCreate(BaseModel):
    name: str
    email: EmailStr
    cedula: str

class VoterResponse(BaseModel):
    id: int
    name: str
    email: str
    cedula: str
    has_voted: bool

    class Config:
        from_attributes = True