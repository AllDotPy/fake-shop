"""
Checkout Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage

# Import your modules here...


class CheckoutPage(FletXPage):
    """Checkout Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Colors.BLACK
        )

        # ...

    def on_init(self):
        """Hook called when CheckoutPage in initialized"""

        print("CheckoutPage is initialized")

    def on_destroy(self):
        """Hook called when CheckoutPage will be unmounted."""

        print("CheckoutPage is destroyed")

    def build(self)-> Control:
        """Method that build CheckoutPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("CheckoutPage works!", size=24),
            ]
        )