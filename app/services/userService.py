from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.userSchema import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token


def create_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    hashed_password = hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, login_data: UserLogin):
    user = db.query(User).filter(
        User.username == login_data.username
    ).first()

    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}