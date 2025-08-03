"""
Shoppingcart Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage

# Import your modules here...


class ShoppingCartPage(FletXPage):
    """Shoppingcart Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...

    def on_init(self):
        """Hook called when ShoppingcartPage in initialized"""

        print("ShoppingcartPage is initialized")

    def on_destroy(self):
        """Hook called when ShoppingcartPage will be unmounted."""

        print("ShoppingcartPage is destroyed")

    def build(self)-> Control:
        """Method that build ShoppingcartPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("ShoppingcartPage works!", size=24),
            ]
        )