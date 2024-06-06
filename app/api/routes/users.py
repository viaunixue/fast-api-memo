from fastapi import APIRouter

from app.models.user import (
    User,
    UserCreate,
    UserLogin
)

router = APIRouter()

# 회원 가입
@router.post("/signup")
async def register_user(signup):
    return

# 로그인
@router.post("/login")
async def login():
    return

# 로그아웃
@router.post("/logout")
async def logout():
    return
