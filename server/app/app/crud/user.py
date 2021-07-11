from typing import Optional

from sqlalchemy.orm import Session

from app.schemas import auth
from app.models.user import User
from app.security import get_password_hash, verify_password


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()


def get_user_by_identifier(db: Session, identifier: str) -> User:
    return db.query(User).filter((User.email == identifier) | (User.username == identifier)).first()


def get_users(db: Session):
    return db.query(User).all()


def create(db: Session, user: auth.UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, username=user.username, full_name=user.full_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, identifier: str, password: str) -> Optional[User]:
    user = get_user_by_identifier(db, identifier=identifier)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user