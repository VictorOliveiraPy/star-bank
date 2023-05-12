from datetime import date
from typing import List

from pydantic import BaseModel


class TransferRule(BaseModel):
    key: str
    value: int


class Transfer(BaseModel):
    amount: int
    tax_id: str
    name: str
    bank_code: str
    branch_code: str
    account_number: str
    external_id: str
    scheduled: date
    tags: List[str]
    rules: List[TransferRule]


class TransferRequest(BaseModel):
    transfers: List[Transfer]
