from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-20",
        "page_count": 352,
        "language": "en"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "en"
    },
    {
        "id": 3,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publisher": "MIT Press",
        "published_date": "2009-07-31",
        "page_count": 1312,
        "language": "en"
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2015-11-01",
        "page_count": 560,
        "language": "en"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModal(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModal) -> dict:
    for book in books:
        if book["id"] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")
