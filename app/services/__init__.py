"""
fakeShop Application Services module.

This module contains Business services and API calls
Version: 0.1.0
"""

# Import your services here..
from .categories_service import CategoriesService
from .products_service import ProductsService
from .user_service import UserService
from .auth_service import AuthService

__all__ = [
    'AuthService',
    'UserService',
    'ProductsService',
    'CategoriesService'
]