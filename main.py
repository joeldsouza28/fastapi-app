from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None) :
    if published:
        return {"data": f"{limit} blogs from the db"}
    else:
        return {"data": f"10 blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": {"unpublished blogs": []}}

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id }

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": {"comments": [1,2]}}



@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"blog is created with title {blog.title}"}