from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import deps
from app import crud
from app import schemas
from app.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(user: schemas.UserAuth, db: Session = Depends(deps.get_db)) -> Any:
    auth_user = crud.authenticate(db, identifier=user.identifier, password=user.password)
    if not auth_user:
        raise (HTTPException(status_code=400, detail="Incorrect Login Details"))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "token_type": "bearer",
        "access_token": create_access_token(
            data={"sub": user.identifier}, expires_delta=access_token_expires
        ),
    }
