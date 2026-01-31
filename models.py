from pydantic import BaseModel

class ProductInput(BaseModel):
    product_name: str
    category: str
    features: str
    target: str
    unique_benefits: str
    price: str
    tone: str