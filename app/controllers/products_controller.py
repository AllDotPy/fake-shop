"""
Products Controller.

This controller class is generated from a template.

🛠️ Customization Guide:
- You can rename or extend this class as needed.
  → Example: Inherit from a different base if you use a custom controller class.
- Add your own reactive attributes using types like `RxInt`, `RxStr`, `RxBool`, etc.
- Implement methods to handle business logic, side effects, or custom events.
- Controllers can be injected into components or apps using dependency injection or manual wiring.
"""

from typing import List, Optional
from fletx import FletX
from fletx.core import (
    FletXController, RxInt
)

from app.models import ProductInfo
from app.services import ProductsService
from app.utils import get_http_error_message

class ProductsController(FletXController):
    """Products Controller"""

    def __init__(self):
        # Defining Product Service
        self.productService: ProductsService = FletX.put(
            ProductsService(), tag = 'product_srv'
        )
        super().__init__()

    def on_initialized(self):
        """Hook called when initializing controller"""
        print("ProductsController initialized.")

    def on_ready(self):
        """Hook called when the controller is ready"""
        print("ProductsController is READY!!!")
    
    def on_disposed(self):
        """Hook called when disposing controller"""
        print("ProductsController is disposing")

    def all(self, page: int = 0) -> List[ProductInfo]:
        """Get All Products."""

        # Set loading state
        self.set_loading(True)
        result = []

        try:
            # Make the request
            res = self.productService.all(page = page)

            if res.ok and res.is_json:
                # Then parse ans return product list
                result = [ProductInfo.from_json(prod) for prod in res.json()]

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def retrieve(self, id: int) -> ProductInfo:
        """Retrieve a product by a given id"""

        # Set loading state
        self.set_loading(True)
        result = None

        try:
            # Make the request
            res = self.productService.retrieve(id)

            if res.ok and res.is_json:
                # Then parse ans return product info
                result = ProductInfo.from_json(res.json())

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def retrieve_by_slug(self, slug: str) -> ProductInfo:
        """Retrieve a product by a given slug"""

        # Set loading state
        self.set_loading(True)
        result = None

        try:
            # Make the request
            res = self.productService.retrieve(slug)

            if res.ok and res.is_json:
                # Then parse ans return product info
                result = ProductInfo.from_json(res.json())

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def filter(
        self,
        title: Optional[str] = None,
        categoryId: Optional[int] = None,
        categorySlug: Optional[str] = None,
        price: Optional[int] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        page: int = 0,
        limit: int = 40,
    ) -> List[ProductInfo]:
        """Filter products"""

        # Set loading state
        self.set_loading(True)
        result = []

        try:
            # Make the request
            res = self.productService.filter(
                title = title, 
                categoryId = categoryId, 
                categorySlug = categorySlug, 
                price = price, 
                price_min = price_min, 
                price_max = price_max, 
                page = page, 
                limit = limit
            )

            if res.ok and res.is_json:
                # Then parse ans return product list
                result = [ProductInfo.from_json(prod) for prod in res.json()]

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def create(self, product: ProductInfo) -> ProductInfo:
        """Create a new product with provided information."""

        # Set loading state
        self.set_loading(True)
        result = None

        try:
            # Make the request
            res = self.productService.create(product)

            if res.ok and res.is_json:
                # Then parse ans return created product info
                result = ProductInfo.from_json(res.json())

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def update(self, id: int, product: ProductInfo) -> ProductInfo:
        """Update product information."""

        # Set loading state
        self.set_loading(True)
        result = None

        try:
            # Make the request
            res = self.productService.update(id, product)

            if res.ok and res.is_json:
                # Then parse ans return updated product info
                result = ProductInfo.from_json(res.json())

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def get_related(self, id: int) -> List[ProductInfo]:
        """Get products related to a product with a given id"""

        # Set loading state
        self.set_loading(True)
        result = []

        try:
            # Make the request
            res = self.productService.get_related(id)

            if res.ok and res.is_json:
                # Then parse ans return related products list
                result = [ProductInfo.from_json(prod) for prod in res.json()]

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def get_slug_related(self, slug: str) -> List[ProductInfo]:
        """Get products related to a product with a given slug"""

        # Set loading state
        self.set_loading(True)
        result = []

        try:
            # Make the request
            res = self.productService.get_slug_related(slug)

            if res.ok and res.is_json:
                # Then parse ans return related products list
                result = [ProductInfo.from_json(prod) for prod in res.json()]

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return result
        
    def delete(self, id: int) -> bool:
        """Delete a product by a given id"""

        # Set loading state
        self.set_loading(True)
        success = False

        try:
            # Make the request
            res = self.productService.delete(id)

            if res.ok:
                success = True

            # If request failed, set error message
            else:
                self.set_error(
                    get_http_error_message(res)
                )

        except Exception as e:
            print(e)
            self.set_error(str(e))
        
        # Close loading state finally
        finally:
            self.set_loading(False)
            return success

# GLOBAL INSTANCE
FletX.put(ProductsController(), tag = 'product_ctrl')
