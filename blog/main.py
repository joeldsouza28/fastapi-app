from fastapi import FastAPI
from .model import Base
from .database import engine
from .routers import blog_router, user_router, login_router

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(blog_router)
app.include_router(user_router)
app.include_router(login_router)




