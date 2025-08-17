from dataclasses import dataclass
from typing import Optional

from .base import BaseModel
from .product import ProductInfo

####
##      CATEGORY INFO
#####
@dataclass
class CartItem(BaseModel):
    """Shopping cart Item representation model."""

    product: ProductInfo
    quantity: Optional[int] = 0
    