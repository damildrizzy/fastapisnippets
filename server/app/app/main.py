from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, users, snippet
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8081",
    "https://fastapisnippets.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(snippet.router, prefix="/snippets", tags=["snippets"])
