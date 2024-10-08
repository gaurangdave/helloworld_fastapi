from fastapi import FastAPI
from typing import Optional
import json

from models import Blog

app = FastAPI()  # creating instance of FastAPI class

with open('data.json', 'r') as file:
    data = json.load(file)

# example of simple get request


@app.get("/blogs/")
def get_items():
    return data.get('blogs')


# Static and Dynamic Path Example
"""
This only works if all static routes like (`/blogs/unpublished`) is before dynamic routes (`/blog/{id}`) 
FastAPI resolves api path in order of implementation.
"""


@app.get("/blogs/unpublished/")
def get_unpublished_blogs():
    # get unpublished blogs
    unpublished_blogs = [blog for blog in data.get(
        'blogs', []) if not blog.get('published', True)]
    return unpublished_blogs


@app.get("/blogs/{id}")
def get_blog_by_id(id: int):
    blog = [blog for blog in data.get('blogs', []) if blog.get('id') == id]
    return blog


# Query Params Example
"""
In example below,
id is a path parameter.
published is required query parameter.
limit is a query parameter with default value of 10.
sub_only is a optional query parameter with no default value.
required query params should be defined before optional query params or default value query params.
"""


@app.get("/blogs/{id}/comments/")
def get_comments(id: int, published: bool, limit: int = 5, sub_only: Optional[bool] = None):
    blog = get_blog_by_id(id)
    if not blog:
        return {"message": "Blog not found"}

    # filter comments by published value
    comments = blog[0].get('comments', [])
    comments = [comment for comment in comments if comment.get(
        'published') == published]

    # if sub_only is defined, filter comments by sub_only value
    if sub_only is not None:
        comments = [comment for comment in comments if comment.get(
            'isSubscriber') == sub_only]

    # limit comments
    limitedComments = comments[:limit]

    return limitedComments

# example of post request with request body


@app.post("/blogs/")
def add_blog(blog: Blog):
    data['blogs'].append(blog.model_dump())
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return blog
