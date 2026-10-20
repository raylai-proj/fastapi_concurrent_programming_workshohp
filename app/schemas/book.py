from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

class BookCreate(BaseModel):
    """The pydantic model to define what data does a book have."""

    # model config: extra data during model initialization is forbidden.
    model_config = ConfigDict(extra="forbid")

    # Field create field for setting data config
    title: str = Field(min_length=1, max_length=256)
    author: str = Field(min_length=1, max_length=256)

    # strict=True make publish_year only accept 1. integer, 2. 1-9999
    publish_year: int | None = Field(ge=1, le=9999, strict=True)

    # regular expression:
    # r"" in pattern = raw python string
    # ^ in pattern = start of the string, $ = end of string
    # (?:...) = non-capture group: grouping is needed in regex logic, but don't need to extract it
    # 0|[1-9] = 0 or one digit 1-9
    # [0-9]* = zero or more digits from 0-9
    # \. = backslash(\) to have .
    # [0-9]{2} = two digit of 0-9 after the decimal point
    price: str | None = Field(pattern=r"^(?:0|[1-9][0-9]*)\.[0-9]{2}$")

    # Literal["USD"] strict currency only accept string "USD" 
    currency: Literal["USD"] | None

    # mode="before" means run function(raw_input) before pydantic parsing, validating
    # classmethod means function receive class object as cls instead of self to run
    # field_validator = validator used to validate field
    @field_validator("title", "author", mode="before")
    @classmethod
    def trim_text(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value

    # mode="after" means run function after input has been validated
    @model_validator(mode="after")
    def validate_price_currency_pair(self) -> "BookCreate":
        if (self.price == None) != (self.currency == None):
            raise ValueError("price and currency must both be set or both be null")
        return self