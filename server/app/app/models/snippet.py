import datetime
from typing import TYPE_CHECKING

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


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
