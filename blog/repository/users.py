from sqlalchemy.orm import Session
from ..model import User
from ..hashing import Hash
from ..schema import User as UserSchema
from fastapi import HTTPException, status


def create(db: Session, request: UserSchema):
    hashed_password = Hash().encrypt(password=request.password)
    data = {"password": hashed_password, **request.model_dump()}
    new_user = User(**data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(db: Session, id: int):
    user = db.query(User).where(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

