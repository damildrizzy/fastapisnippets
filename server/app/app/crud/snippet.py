from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.snippet import Snippet
from ..schemas.snippet import SnippetCreate

from app.models.user import User


def get_snippet(db: Session, snippet_id: int) -> Snippet:
    return db.query(Snippet).filter(Snippet.id == snippet_id).first()


def get_snippets(db: Session):
    return db.query(Snippet).all()


def get_top_authors(db: Session):
    return db.query(User, func.count(User.snippets).label("count")).all()


def create(db: Session, snippet: SnippetCreate, user_id: int):
    db_snippet = Snippet(**snippet.dict(), author_id=user_id)
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet
