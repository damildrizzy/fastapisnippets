from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas
from app.security import get_password_hash, verify_password


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_identifier(db: Session, identifier: str) -> models.User:
    return db.query(models.User).filter((models.User.email == identifier) | (models.User.username == identifier)).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.auth.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email,
                          username=user.username, full_name=user.full_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, identifier: str, password: str) -> Optional[models.User]:
    user = get_user_by_identifier(db, identifier=identifier)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
