from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List

from ..crud.user import create_user, get_user_by_email, get_users, get_user
from ..schemas import auth
from .deps import get_db

router = APIRouter()


@router.post("/", response_model=auth.User)
def create_user(user: auth.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/", response_model=List[auth.User])
def list_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


@router.get("/users/{user_id}", response_model=auth.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
