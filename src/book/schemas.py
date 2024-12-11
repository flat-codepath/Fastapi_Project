from fastapi import   Request
from  pydantic import BaseModel

class Book(BaseModel):
  id: int
  title: str
  author: str
  genre: str
  year: int
  publisher: str
  ISBN: str

class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    publisher: str
    ISBN: str
