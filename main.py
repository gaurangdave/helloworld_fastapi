from fastapi import FastAPI

app = FastAPI()

# example of sime get request
@app.get("/items/")
def get_items():
    return {"items": [{"name": "Item One"}, {"name": "Item Two"}]}


@app.get("/blog/{id}")
def get_blog_by_id(id: int):
    return {"blog": {"title": f"Blog Number {id}", "content": "Blog Content"}}