from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# 기존 라우트 
@router.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})
    
@router.get("/about")
async def about():
    return {"message": "이것은 마이 메모 앱 소개 페이지 입니다."}