"""
Shoppingcart Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx import FletX
from fletx.core import FletXPage, RxList
from fletx.widgets import Obx

# Import your modules here...
from app.controllers import (
    ProductsController,
    OrderController
)
from app.models import CartItem, OrderInfo
from app.components import CartItemlist
from app.utils import show_snackbar


class ShoppingCartPage(FletXPage):
    """Shoppingcart Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 10,
                vertical = 0,
            ),
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...
        self.productsController: ProductsController = FletX.find(
            ProductsController, tag = 'product_ctrl'
        )
        self.ordersController: OrderController = FletX.find(
            OrderController, tag = 'order_ctrl'
        )
        self.items: RxList[CartItem] = self.productsController.create_rx_list(
            [item for item in self.productsController.shopping_cart.value.values()]
        )

    def on_init(self):
        """Hook called when ShoppingcartPage in initialized"""

        print("ShoppingcartPage is initialized")
        self.productsController.shopping_cart.listen(
            lambda: self.rebuild_items()
        )

    def on_destroy(self):
        """Hook called when ShoppingcartPage will be unmounted."""

        print("ShoppingcartPage is destroyed")

    def rebuild_items(self):
        """Rebuild items list"""
        self.items.clear()
        self.items.extend(
                [item for item in self.productsController.shopping_cart.value.values()]
            ) 
        
    @property
    def total(self):
        """Return total amount"""
        return sum(
            [
                item.quantity * item.product.price 
                for item 
                in self.items
            ]
        )
    
    def build_order(self):
        """Build Order Object from Items."""

        order = OrderInfo(
            articles = self.items.value,
        )
        return order
    
    def save_order(self):
        """Create an Order"""

        res = self.ordersController.create(
            self.build_order()
        )
        if res:
            # Then Show A Success Popup
            show_snackbar(
                self.page_instance, 
                title = "Order Successful", 
                message = "You have successfully made Order.", 
                type = 'success'
            )


    def build(self)-> Control:
        """Method that build ShoppingcartPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.START,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                # HEADER
                Row(
                    width = self.width,
                    # height = 60,
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment = CrossAxisAlignment.CENTER,
                    controls = [
                        Text(
                            f"My Shopping Cart",
                            size = 16,
                            weight = FontWeight.BOLD
                        ),
                    ]
                ),

                # ITEMS
                Container(
                    expand = True,
                    width = self.width,
                    # bgcolor = 'red',
                    content = CartItemlist(
                        expand = True,
                        spacing = 10,
                        items = self.items
                    )
                ),

                # Divider
                Divider(
                    thickness = 2,
                    color = Colors.with_opacity(
                        .4,
                        Colors.ON_SURFACE
                    )
                ),

                # SUMMARY
                Obx(
                    builder_fn = lambda: Container(
                        height= 120,
                        width = self.width,
                        visible = len(self.items) > 0,
                        content = Column(
                            controls = [
                                Text(
                                    f"Total items {len(self.items)}",
                                    size = 16,
                                    weight = FontWeight.W_400
                                ),

                                # TOTAL PRICE
                                Row(
                                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                                    controls = [
                                        Text(
                                            f"Total Amount",
                                            size = 16,
                                            weight = FontWeight.BOLD
                                        ),
                                        Obx(
                                            builder_fn = lambda: Text(
                                                f"{self.total} FCFA",
                                                size = 16,
                                                weight = FontWeight.BOLD
                                            ),
                                        ),
                                    ]
                                ),

                                # CHECKOUT ORDER
                                Obx(
                                    builder_fn = lambda: OutlinedButton(
                                        width = self.width,
                                        height = 50,
                                        expand = True,
                                        style = ButtonStyle(
                                            bgcolor = Colors.PRIMARY,
                                        ),
                                        content = Row(
                                            alignment = MainAxisAlignment.CENTER,
                                            controls = [
                                                ProgressRing(
                                                    height = 30,
                                                    width = 30,
                                                    color = Colors.ON_PRIMARY
                                                ) if self.ordersController._is_loading.value else Container(),
                                                Text(
                                                    f'Checkout {self.total} FCFA',
                                                    size = 16,
                                                    color = Colors.ON_PRIMARY,
                                                    weight = FontWeight.W_500
                                                ),
                                                Icon(
                                                    Icons.ARROW_FORWARD,
                                                    color = Colors.ON_PRIMARY
                                                ),
                                            ]
                                        ),
                                        on_click = lambda _: self.save_order() if not self.ordersController._is_loading.value else None,
                                    ),
                                ),
                            ]
                        )
                    ),
                ),
                

                # Text(f"ShoppingcartPage works! {len(self.productsController.shopping_cart.value)}", size=24),
            ]
        )