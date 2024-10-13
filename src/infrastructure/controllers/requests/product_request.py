from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    price: float
    description: str