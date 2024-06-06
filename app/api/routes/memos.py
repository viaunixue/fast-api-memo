from fastapi import FastAPI, APIRouter, Request, Depends

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from app.api.deps import (
    get_db    
)

from app.models.memo import (
    Memo,
    MemoCreate,
    MemoUpdate
)

router = APIRouter()

# 메모 생성
@router.post("/")
async def create_memo(memo: MemoCreate, db: Session = Depends(get_db)):
    new_memo = Memo(title=memo.title, content=memo.content)
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo)
    return ({"id": new_memo.id, "title": new_memo.title, "content": new_memo.content})

# 메모 조회
@router.get("/")
async def list_memos(db: Session = Depends(get_db)):
    memos = db.query(Memo).all()
    return [{"id": memo.id, "title": memo.title, "content": memo.content} for memo in memos]

# 메모 수정
@router.put("/{memo_id}")
async def update_memo(memo_id: int, memo: MemoUpdate, db: Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    if memo.title is not None:
        db_memo.title = memo.title
    if memo.content is not None:
        db_memo.content = memo.content
    
    db.commit()
    db.refresh()
    return ({"id": db_memo.id, "title": db_memo.title, "content": db_memo.content})

# 메모 삭제
@router.delete("/{memo_id}")
async def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    
    db.delete(db_memo)
    db.commit()
    return ({"message": "Memo deleted"})