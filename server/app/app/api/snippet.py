from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from typing import List

from .deps import get_db, get_current_user
from app import schemas
from app import models
from app import crud

router = APIRouter()


@router.get("/", response_model=List[schemas.Snippet])
def list_snippets(db: Session = Depends(get_db)):
    snippets = crud.read_snippets(db)
    return snippets


@router.get("/top-authors", response_model=List[schemas.TopAuthors])
def top_authors(db: Session = Depends(get_db)):
    return crud.read_top_authors(db)


@router.get("/{snippet_id}", response_model=schemas.Snippet)
def get_snippet(snippet_id: int, db: Session = Depends(get_db)):
    db_snippet = crud.read_snippet(db, snippet_id=snippet_id)
    if db_snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return db_snippet


@router.post("/", response_model=schemas.Snippet)
def create_snippet(
        snippet: schemas.SnippetCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)):
    return crud.create_snippet(db, snippet, user_id=current_user.id)

