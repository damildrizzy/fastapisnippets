from datetime import datetime
from pydantic import BaseModel
from .auth import User


class SnippetBase(BaseModel):
    title: str
    description: str
    code: str


class SnippetCreate(SnippetBase):
    pass


class Snippet(SnippetBase):
    id: int
    author_id: int
    author: User
    pub_date: datetime
    updated_at: datetime = None

    class Config:
        orm_mode = True
