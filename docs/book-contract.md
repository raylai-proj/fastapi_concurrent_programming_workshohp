# Book API contract

## Create a book

Client-supplied fields: `title`, `author`, `publish_year`, `price`, `currency`.
The server generates `book_id`; clients must not provide it.

Example request:

```json
{
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.50",
    "currency": "USD"
}

{
    "title": "Example Book",
    "author": "Ursula K. Le Guin",
    "publish_year": null,
    "price": null,
    "currency": null
}
```

Example response:
```json
{
    "book_id": 1,
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.50",
    "currency": "USD"
}
```