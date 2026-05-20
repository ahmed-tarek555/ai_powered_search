from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):

    name: str
    description: str
    price: Decimal
    category: str