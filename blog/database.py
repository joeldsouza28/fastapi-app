from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

SQLALCHEMY_DATABASE = "sqlite:///./blog.db"

engine = create_engine("sqlite:///./blog.db", connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
