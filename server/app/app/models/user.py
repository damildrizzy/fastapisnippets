from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    snippets = relationship("Snippet", back_populates="author")
    is_admin = Column(Boolean, default=False)
