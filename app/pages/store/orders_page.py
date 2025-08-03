"""
Orders Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage

# Import your modules here...


class OrdersPage(FletXPage):
    """Orders Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...

    def on_init(self):
        """Hook called when OrdersPage in initialized"""

        print("OrdersPage is initialized")

    def on_destroy(self):
        """Hook called when OrdersPage will be unmounted."""

        print("OrdersPage is destroyed")

    def build(self)-> Control:
        """Method that build OrdersPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("OrdersPage works!", size=24),
            ]
        )