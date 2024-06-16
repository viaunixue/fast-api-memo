from fastapi import APIRouter

from app.api.routes import memos, users, test

api_router = APIRouter()

# api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(memos.router, prefix="/memos", tags=["memos"])
api_router.include_router(users.router, prefix="/users", tags=["users"])