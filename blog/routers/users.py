from fastapi import APIRouter, Depends, status, HTTPException
from ..schema import ShowUser, User
from ..database import get_db
from ..model import User as UserModel
from sqlalchemy.orm import Session
from ..repository import users


user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.post("/", response_model=ShowUser)
def create(request: User, db: Session = Depends(get_db)):
    return users.create(db=db, request=request)


@user_router.get("/{id}", response_model=ShowUser)
def get(id:int, db: Session = Depends(get_db)):
    return users.get(db=db, id=id)