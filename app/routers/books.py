from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"}
]

@router.get("/books", response_model=List[dict])
def get_books():
    return books_db

@router.post("/books")
def add_book(book: dict):
    book["id"] = len(books_db) + 1
    books_db.append(book)
    return book

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
