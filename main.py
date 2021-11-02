from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"ttile": "titile of post", "content": "content of post","id":1}]


@app.get("/")
def get_user():
    return {"a": "b"}


@app.post("/create")
def create(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
