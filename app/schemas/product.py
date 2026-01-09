from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import ConfigDict


class ProductBase(SQLModel):
    name: str = Field(min_length=1, max_length=255, index=True)
    description: Optional[str] = Field(default=None, max_length=1000)
    price: int = Field(default=0, ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    price: Optional[int] = Field(default=None, ge=0)


class ProductRead(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
