from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    pages: int
    genre: str

class User(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: list[Book]