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

**Example request with unknown values:**

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

**Invalid Example request: `title` must be a string, not `null`**

```json
{
    "title": null,
    "author": "Example Writer",
    "publish_year": 2021,
    "price": "10.00",
    "currency": "USD"
}
```

**Invalid Example request: `author` must be a string., not `null`**

```json
{
    "title": "Example title",
    "author": null,
    "publish_year": 2027,
    "price": "50.00",
    "currency": "USD"
}
```

**Invalid Example request: the client must not supply `book_id`.**

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

**Invalid Example request: `price` and `currency` must both be known or both be `null`.**

```json
{
    "title": "Example title",
    "author": "Example Writer",
    "publish_year": 2034,
    "price": null,
    "currency": "USD"
}
```

## Field rules

| Field | Create request rule | Response rule |
|---|---|---|
| `book_id` | Must not be supplied by client | Server-generated integer |
| `title` | Required string; trim surrounding whitespace; reject blank values; maximum 256 characters | String |
| `author` | Required single string; trim surrounding whitespace; reject blank values; maximum 256 characters | String |
| `publish_year` | Required key; integer from 1 to 9999, or `null`; future years are allowed | Integer or `null` |
| `price` | Required key; non-negative decimal string with exactly two fractional digits, or `null` | Decimal string or `null` |
| `currency` | Required key; `"USD"` or `null`; must be `null` exactly when `price` is `null` | `"USD"` or `null` |

Unknown fields are rejected. `price` and `currency` must either both have values or both be `null`.