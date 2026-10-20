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

**Invalid Example request: `author` must be a string, not `null`**

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

**Invalid Example request: `title` must not be blank.**

```json
{
    "title": "   ",
    "author": "Example Writer",
    "publish_year": 2034,
    "price": null,
    "currency": "USD"
}
```

**Invalid Example request: `author` must not be blank.**

```json
{
    "title": "Example title",
    "author": "   ",
    "publish_year": 2034,
    "price": null,
    "currency": "USD"
}
```

**Invalid Example request: `price` must have exactly two digits after the decimal point.**

```json
{
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12",
    "currency": "USD"
}
```

**Invalid Example request: `currency` must be `"USD"`**

```json
{
    "title": "Example Title",
    "author": "A. Writer",
    "publish_year": 2030,
    "price": "12.00",
    "currency": "EUR"
}
```

## Field rules

| Field | Create request rule | Response rule |
|---|---|---|
| `book_id` | Must not be supplied by the client | Server-generated integer |
| `title` | Required string. Trim leading and trailing whitespace first; reject the value if it is empty after trimming; then require the trimmed value to be no longer than 256 characters. | Trimmed string |
| `author` | Required single string. Trim leading and trailing whitespace first; reject the value if it is empty after trimming; then require the trimmed value to be no longer than 256 characters. | Trimmed string |
| `publish_year` | Required key; integer from 1 to 9999, or `null`; future years are allowed | Integer or `null` |
| `price` | Required key; must be a non-negative decimal string with exactly two digits after the decimal point, such as "12.50", or `null` | Decimal string or `null` |
| `currency` | Required key; `"USD"` or `null`; must be `null` exactly when `price` is `null` | `"USD"` or `null` |

Unknown fields are rejected. `price` and `currency` must either both have values or both be `null`.

### Invalid examples
**Invalid Example request: the client must not supply `unexpected` field**

```json
{
    "unexpected": "value",
    "title": "Example title",
    "author": "A.Writer",
    "publish_year": 2027,
    "price": "50.00",
    "currency": "USD"
}
```