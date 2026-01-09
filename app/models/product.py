from sqlmodel import SQLModel, Field
from typing import Optional


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, max_length=255)
    description: Optional[str] = Field(default=None)
    price: int = Field(default=0, ge=0)
