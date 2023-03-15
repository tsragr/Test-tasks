from pydantic import BaseModel


class Article(BaseModel):
    article: int
    brand: str
    title: str
