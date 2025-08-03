from dataclasses import dataclass
from typing import Optional

from .base import BaseModel

####
##      CATEGORY INFO
#####
@dataclass
class CategoryInfo(BaseModel):
    """Category representation model."""

    name: str
    image: Optional[str] = None
    slug: Optional[str] = None
    id: Optional[str] = None

