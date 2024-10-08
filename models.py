from typing import Optional, List, Dict, Union

from pydantic import BaseModel


class Comment(BaseModel):
    value: str
    published: Optional[bool] = True
    isSubscriber: Optional[bool] = False


class Blog(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    comments: List[Comment]     = []
