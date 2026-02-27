from fastapi import FastAPI
from sqlalchemy import text
from app.config import settings
from app.database.connection import engine

from app.routers import voter, candidate, votes, user

app = FastAPI(
    title=settings.PROJECT_NAME,
)

@app.get("/")
def root():
    return {
        "message": "Corriendo API Sistema de Votación",
    }

app.include_router(user.router)
app.include_router(voter.router)
app.include_router(candidate.router)
app.include_router(votes.router)

@app.on_event("startup")
def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Conexión exitosa a PostgreSQL")
    except Exception as e:
        print("Error de conexión:", e)