from fastapi import APIRouter, status, Depends
from ..schema import Blog, ShowBlog, User
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

blog_router = APIRouter(prefix="/blog", tags=["blogs"])


@blog_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Blog)
def create(
    request: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog.create(db=db, data={**request.model_dump()})


@blog_router.get("/", response_model=List[ShowBlog])
def get_all(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return blog.get_all(db=db)


@blog_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog.show(db=db, id=id)


@blog_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return blog.delete(db=db, id=id)


@blog_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    blog.update(db=db, id=id)
    return "done"
