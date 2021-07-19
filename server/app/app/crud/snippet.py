from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models, schemas


def read_snippet(db: Session, snippet_id: int) -> models.Snippet:
    return db.query(models.Snippet).filter(models.Snippet.id == snippet_id).first()


def read_snippets(db: Session):
    return db.query(models.Snippet).all()


def read_top_authors(db: Session):
    return db.query(models.User, func.count(models.User.snippets).label("count")).all()


def create_snippet(db: Session, snippet: schemas.SnippetCreate, user_id: int):
    db_snippet = models.Snippet(**snippet.dict(), author_id=user_id)
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet
