from fastapi import  APIRouter,status
from fastapi.exceptions import  HTTPException
from src.book.schemas import Book,BookUpdate
from src.book.book_data import  books
from typing import  List
book_router =APIRouter()

@book_router.get('/' ,response_model=List[Book])
def  get_all_books():
   return books

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async  def create_a_book( book_data:Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/{book_id}")
def get_book(book_id:int)->dict:
    for book in books:
      if book["id"]== book_id:
        return book
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail='books not found')

@book_router.patch('/{book_id}')
def update_book(book_update_data:BookUpdate,book_id=int ):
       for book in books:
         if book['id']== book_id:
             book['title']=book_update_data.title
             book['auther']=book_update_data.auther
             book['genre']=book_update_data.genre
             book["year"]=book_update_data.year
             book["publisher"]=book_update_data.publisher
             book["ISBN"]=book_update_data.ISBN
             return  book
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")

@book_router.delete("/{book_id}")
def delete_book(book_id:int)->dict:
   for book in books:
     if book['id']== book_id:
       books.remove(book)
       return {}


# A better file structure with Routers

