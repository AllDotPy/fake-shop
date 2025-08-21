from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, List, Union

from .base import BaseModel
from .cart_item import CartItem
from .user import UserInfo


####
##      ORDER STATUS ENUM
#####
class OrderStatus(str, Enum):
    """Order available status"""

    WAITING_FOR_PAYMENT = 'WAITING_FOR_PAYMENT'
    DELIVERING = 'DELIVERING'
    COMPLETED = 'COMPLETED'


####
##      ORDER INFO
#####
@dataclass
class OrderInfo(BaseModel):
    """Order representation model."""

    articles: List[CartItem]
    client: Optional[UserInfo] = None
    total: Optional[int] = 0
    status: Union[OrderStatus,str] = OrderStatus.WAITING_FOR_PAYMENT
    id: Optional[str] = None
    code: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    