from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException

from sqlalchemy.orm import Session

from app.api.deps import get_db    
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import get_password_hash, verify_password

router = APIRouter()

# 회원 가입
@router.post("/signup")
async def register_user(signup_data: UserCreate, db: Session = Depends(get_db)):
    # username 존재 여부 확인
    existing_user = db.query(User).filter(User.username == signup_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 동일 사용자 이름이 가입되어 있습니다!")
    
    hashed_password = get_password_hash(signup_data.password)
    new_user = User(username=signup_data.username, email=signup_data.email, hashed_password=hashed_password)
    db.add(new_user)

    try:
        db.commit()
    except Exception as e:
        print (e)
        raise HTTPException(status_code=500, detail="회원가입이 실패했습니다. 기입한 내용을 확인해보세요!")
    
    db.refresh(new_user)
    return {"message": "회원가입이 성공했습니다!"}

# 로그인
@router.post("/login")
async def login(request: Request, signin_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == signin_data.username).first()
    if user and verify_password(signin_data.password, user.hashed_password):
        request.session["username"] = user.username
        return {"message": "로그인이 성공하였습니다!"}
    else:
        raise HTTPException(status_code=401, detail="로그인이 실패했습니다!")

# 로그아웃
@router.post("/logout")
async def logout(request: Request):
    request.session.pop("username", None)
    return {"message": "로그아웃이 성공했습니다!"}
