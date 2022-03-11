from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas


def read_snippet(db: Session, snippet_id: int) -> models.Snippet:
    return db.query(models.Snippet).filter(models.Snippet.id == snippet_id).first()


def read_snippets(db: Session):
    return db.query(models.Snippet).all()


def create_snippet(db: Session, snippet: schemas.SnippetCreate, user_id: int):
    db_snippet = models.Snippet(title=snippet.title, description=snippet.description,
                                code=snippet.code, author_id=user_id)

    for tag in snippet.tags:
        db_tag = models.Tag(name=tag)
        db_snippet.tags.append(db_tag)

    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet


def read_top_authors(db: Session):
    snippets = db.query(models.Snippet.author_id, func.count('*').label("count")). \
        group_by(models.Snippet.author_id).subquery()

    query = db.query(models.User, snippets.c.count). \
        outerjoin(snippets, models.User.id == snippets.c.author_id). \
        order_by(snippets.c.count.desc()).limit(5)

    for obj, count in query:
        obj.count = count
        yield obj
