from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud, deps
from app.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(user: schemas.UserAuth, db: Session = Depends(deps.get_db)) -> Any:
    user = crud.authenticate(db, identifier=user.identifier, password=user.password)
    if not user:
        raise (HTTPException(status_code=400, detail="Incorrect Login Details"))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "token_type": "bearer",
        "access_token": create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        ),
    }
