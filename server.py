from fastapi import FastAPI

api = FastAPI()

# example of sime get request
@api.get("/items/")
def get_items():
    return {"items": [{"name": "Item One"}, {"name": "Item Two"}]}


@api.get("/blog/{id}")
def get_blog_by_id(id: int):
    return {"blog": {"title": f"Blog Number {id}", "content": "Blog Content"}}