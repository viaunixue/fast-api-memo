from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.api.deps import get_db    
from app.models.memo import Memo
from app.schemas.memo import MemoCreate, MemoUpdate
from app.models.user import User


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

# 메모 생성
@router.post("/")
async def create_memo(request: Request, memo: MemoCreate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_memo = Memo(user_id=user.id, title=memo.title, content=memo.content)
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)

    # return ({"id": new_memo.id, "title": new_memo.title, "content": new_memo.content})
    return new_memo

# 메모 조회
@router.get("/")
async def list_memos(request: Request, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    memos = db.query(Memo).filter(Memo.user_id == user.id).all()
    
    # return [{"id": memo.id, "title": memo.title, "content": memo.content} for memo in memos]
    return templates.TemplateResponse("memos.html", {"request": request, "memos": memos, "username": username})

# 메모 수정
@router.put("/{memo_id}")
async def update_memo(request: Request, memo_id: int, memo: MemoUpdate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_memo = db.query(Memo).filter(Memo.user_id == user.id, Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    
    if memo.title is not None:
        db_memo.title = memo.title
    if memo.content is not None:
        db_memo.content = memo.content
    
    db.commit()
    db.refresh(db_memo)
    
    # return ({"id": db_memo.id, "title": db_memo.title, "content": db_memo.content})
    return db_memo

# 메모 삭제
@router.delete("/{memo_id}")
async def delete_memo(request: Request, memo_id: int, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    
    db.delete(db_memo)
    db.commit()
    return ({"message": "Memo deleted"})