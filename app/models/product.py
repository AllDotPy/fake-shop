from dataclasses import dataclass, field
from typing import Optional, List

from .base import BaseModel
from .category import CategoryInfo

####
##      PRODUCT INFO
#####
@dataclass
class ProductInfo(BaseModel):
    """User representation model."""

    title: str
    slug: str
    price: int
    category: CategoryInfo
    desctiotion: Optional[str] = None
    images: List[str] = field(default_factory = list)
    id: Optional[str] = None
