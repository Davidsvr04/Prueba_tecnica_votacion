from fastapi import FastAPI
from app.config import settings
from sqlalchemy import text
from app.database.connection import engine

app = FastAPI(
    title=settings.PROJECT_NAME,
)

@app.get("/")
def root():
    return {
        "message": "Corriendo API Sistema de Votación",
    }

@app.on_event("startup")
def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Conexión exitosa a PostgreSQL")
    except Exception as e:
        print("Error de conexión:", e)