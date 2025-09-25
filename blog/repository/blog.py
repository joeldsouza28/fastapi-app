
from sqlalchemy.orm import Session
from ..model import Blog
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create(db: Session, data: dict):
    new_blog = Blog(**data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session, id: int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    
    blog.delete(synchronize_session=False)
    db.commit()
    db.close()


def update(db: Session, id: int, request: dict):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    
    blog.update({**request.model_dump()})
    db.commit()
    db.close()


def show(db: Session, id: int):
    blog = db.query(Blog).where(Blog.id== id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    return blog
