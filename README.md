# Sistema de Votaciones API

## Tecnologías
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication

## Instalación
pip install -r requirements.txt

## Configurar variables de entorno
DATABASE_URL=postgresql://usuario:password@localhost:5432/votaciones

## Modelo de datos

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE voters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    has_voted BOOLEAN DEFAULT FALSE,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE candidates (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    party VARCHAR(100),
    votes INTEGER DEFAULT 0,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    voter_id INTEGER NOT NULL,
    candidate_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_voter FOREIGN KEY (voter_id) REFERENCES voters(id) ON DELETE CASCADE,
    CONSTRAINT fk_candidate FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
    CONSTRAINT unique_vote UNIQUE (voter_id)
);
```

- Se agrego campo de cedula para mejor validacion de que un candidato no pueda ser un votante y viceversa 

## Ejecutar
uvicorn app.main:app --reload

## Documentación
La API estará disponible en: `http://localhost:8000`
(Swagger): http://localhost:8000/docs

## Endpoints principales
- /users/register
- /users/login
- /voters
- /candidates
- /votes
- /votes/statistics

## Ejemplos de uso del API

- Registrar usuario

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "password123"
  }'
```

- Login y obtener token

```bash
curl -X POST "http://localhost:8000/users/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "password123"
  }'
```

- Registrar Votante (Protegido)

```bash
curl -X POST "http://localhost:8000/voters/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "cedula": "12345678"
  }'
```

- Registrar un candidato (Protegido)

```bash
curl -X POST "http://localhost:8000/candidates/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "name": "María López",
    "cedula": "87654321",
    "party": "Partido Central"
  }'
```

- Ralizar voto (Protegido)

```bash
curl -X POST "http://localhost:8000/votes/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "voter_id": 1,
    "candidate_id": 1
  }'
```

- Obtener estadisticas

```bash
curl -X GET "http://localhost:8000/votes/statistics" \
  -H "Content-Type: application/json"
```