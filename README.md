# Sistema de Votaciones API

## Tecnologías
- FastAPI
- PostgreSQL
- SQLAlchemy

## Instalación
pip install -r requirements.txt

## Configurar variables de entorno
DATABASE_URL=postgresql://usuario:password@localhost:5432/votaciones

## Modelo de datos

CREATE TABLE voters (
id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
cedula VARCHAR(20) UNIQUE NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
has_voted BOOLEAN NOT NULL DEFAULT FALSE,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE candidates (
id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
cedula VARCHAR(20) UNIQUE NOT NULL,
party VARCHAR(100),
votes INTEGER NOT NULL DEFAULT 0,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    voter_id INTEGER NOT NULL,
    candidate_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_voter
        FOREIGN KEY (voter_id)
        REFERENCES voters(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES candidates(id)
        ON DELETE CASCADE,

    CONSTRAINT unique_vote UNIQUE (voter_id)
);

- Se agrego campo de cedula para mejor validacion de que un candidato no pueda ser un votante y viceversa 

## Ejecutar
uvicorn app.main:app --reload

## Documentación
http://localhost:8000/docs

## Endpoints principales
- /voters
- /candidates
- /votes
- /votes/statistics

## Ejemplos de uso del API
- Registrar Votante

curl -X POST "http://localhost:8000/voters" \
-H "Content-Type: application/json" \
-d '{
  "name": "Juan Perez",
  "email": "juan@example.com",
  "cedula": "123456789"
}''

- Registrar un candidato

curl -X POST "http://localhost:8000/candidates" \
-H "Content-Type: application/json" \
-d '{
  "name": "Maria Lopez",
  "party": "Partido Central",
  "cedula": "987654321"
}'

- Ralizar voto

curl -X POST "http://localhost:8000/votes" \
-H "Content-Type: application/json" \
-d '{
  "voter_id": 1,
  "candidate_id": 1
}'

- Obtener estadisticas

curl -X GET "http://localhost:8000/votes/statistics"