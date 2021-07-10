from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from typing import List

from .deps import get_db
from ..schemas import snippet
from ..crud.snippet import get_snippets, get_snippet, create_snippet

router = APIRouter()


@router.get("/", response_model=List[snippet.Snippet])
def list_snippets(db: Session = Depends(get_db)):
    snippets = get_snippets(db)
    return snippets


@router.get("/{snippet_id}", response_model=snippet.Snippet)
def read_snippet(snippet_id: int, db: Session = Depends(get_db)):
    db_snippet = get_snippet(db, snippet_id=snippet_id)
    if db_snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return db_snippet


@router.post("/", response_model=snippet.Snippet)
def create_snippet(snippet: snippet.SnippetCreate, db: Session = Depends(get_db)):
    return create_snippet(db, snippet=snippet)
