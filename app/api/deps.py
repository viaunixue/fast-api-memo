from fastapi import FastAPI, Request, Depends

from sqlalchemy.orm import Session

from app.core.db import engine, AsyncSessionLocal
from app.models import memo

async def get_db():
    # db = Session(bind=engine)
    # try:
    #     yield db
    # finally:
    #     db.close()
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()
        # with을 사용하면 알아서 session을 닫아줌
        # await session.close()