from fastapi import APIRouter, status
from app.schemas.book import BookCreate, BookRead
from app.services.books import create_book_record

router = APIRouter(prefix="/books")

@router.post("", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate) -> BookRead:
    """
    1. accept the validated request
    2. call the creat-book service
    3. return saved book with its database-generated ID
    """
    return await create_book_record(book)