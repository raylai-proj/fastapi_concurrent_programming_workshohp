# Book API contract

## Create a book

Client-supplied fields: `title`, `author`, `publish_year`, `price`, `currency`.
The server generates `book_id`; clients must nod provide it.

Example request:

{
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.50",
    "currency": "USD"
}

Example response:

{
    "book_id": 1,
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.50",
    "currency": "USD"
}