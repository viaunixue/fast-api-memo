from fastapi import FastAPI, Request, Depends

from sqlalchemy.orm import Session

from app.core.db import engine
from app.models import memo

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()