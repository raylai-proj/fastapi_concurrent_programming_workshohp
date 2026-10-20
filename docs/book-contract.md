# Book API contract

## Create a book

Client-supplied fields: `title`, `author`, `publish_year`, `price`, `currency`.
The server generates `book_id`; clients must not provide it.

**Example request:**

```json
{
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.50",
    "currency": "USD"
}
```

```json
{
    "title": "Example Book",
    "author": "Ursula K. Le Guin",
    "publish_year": null,
    "price": null,
    "currency": null
}
```

**Example response:**
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

**Invalid Example request:**

```json
{
    "title": null,
    "author": "Example Writer",
    "publish_year": 2021,
    "price": "10.00",
    "currency": "USD"
}
```

```json
{
    "title": "Example title",
    "author": null,
    "publish_year": 2027,
    "price": "50.00",
    "currency": "USD"
}
```

```json
{
    "book_id": 3,
    "title": "Example title",
    "author": "Example Writer",
    "publish_year": 2027,
    "price": "50.00",
    "currency": "USD"
}
```

```json
{
    "title": "Example title",
    "author": "Example Writer",
    "publish_year": 2034,
    "price": null,
    "currency": "USD"
}
```