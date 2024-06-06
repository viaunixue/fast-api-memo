from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(200))
    hashed_password = Column(String(512))

# 회원 가입 시 데이터 검증
class UserCreate(BaseModel):
    username: str
    email: str
    password: str   # unhashed password  

# 회원 로그인 시 데이터 검증
class UserLogin(BaseModel):
    username: str
    password: str   # unhashed password

