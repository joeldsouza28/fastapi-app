from fastapi import APIRouter, Depends, HTTPException, status
from ..schema import Token
from ..database import get_db
from sqlalchemy.orm import Session
from ..model import User
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from ..repository.token import create_access_token
from typing import Annotated

login_router = APIRouter(tags=["authentication"])


@login_router.post("/login", response_model=Token)
def login(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    if not Hash().verify(
        plain_password=request.password, hashed_password=user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password"
        )

    access_token = create_access_token(data={"email": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
