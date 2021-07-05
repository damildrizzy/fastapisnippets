from typing import Optional
from pydantic import BaseModel


class UserAuth(BaseModel):
    identifier: str
    password: str


class UserBase(BaseModel):
    email: str
    username: str
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None


class TongueBase(BaseModel):
    raw_string: str
