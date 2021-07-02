from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserAuth(UserBase):
    password: str


class UserCreate(UserBase):
    full_name: str
    password: str


class User(UserBase):
    id: int
    full_name: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None


class TongueBase(BaseModel):
    raw_string: str
