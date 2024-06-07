from pydantic import BaseModel

# 회원 가입 시 데이터 검증
class UserCreate(BaseModel):
    username: str
    email: str
    password: str   # unhashed password  

# 회원 로그인 시 데이터 검증
class UserLogin(BaseModel):
    username: str
    password: str   # unhashed password