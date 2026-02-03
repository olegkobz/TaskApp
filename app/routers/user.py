from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])
@router.post("/", response_model=schemas.UserRead)
def create_user_endpoint(user:schemas.UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)