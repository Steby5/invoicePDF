from pydantic import BaseModel
from typing import List

class LineItem(BaseModel):
    description: str
    quantity: int
    price: float

class Invoice(BaseModel):
    invoice_number: str
    date: str
    billing_details: str
    line_items: List[LineItem]
    total_amount: float
