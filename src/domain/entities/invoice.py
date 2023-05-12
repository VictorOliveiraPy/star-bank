from datetime import datetime
from typing import List

from pydantic import BaseModel


class InvoiceDescription(BaseModel):
    key: str
    value: str


class InvoiceDiscount(BaseModel):
    percentage: float
    due: datetime


class Invoice(BaseModel):
    amount: int
    descriptions: List[InvoiceDescription]
    discounts: List[InvoiceDiscount]
    due: datetime
    expiration: int
    fine: float
    interest: float
    name: str
    tags: List[str]
    tax_id: str
