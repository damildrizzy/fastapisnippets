import datetime
from typing import TYPE_CHECKING

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

snippet_tag_relation = Table('snippet_tag_relation', Base.metadata,
                             Column('snippet_id', ForeignKey('snippets.id'), primary_key=True),
                             Column('tag_id', ForeignKey('tags.id'), primary_key=True)
                             )


class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    code = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="snippets")
    pub_date = Column(DateTime, default=datetime.datetime.utcnow)
    updated_date = Column(DateTime)
    tags = relationship("Tag", secondary="snippet_tag_relation", back_populates="snippets")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    snippets = relationship("Snippet", secondary="snippet_tag_relation", back_populates="tags")
