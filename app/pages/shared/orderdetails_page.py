"""
Orderdetails Controller.

This Page class is generated from a template.
"""

from flet import *
from typing import Optional
from fletx.core import FletXPage
from fletx.navigation import go_back

# Import your modules here...
from app.models import OrderInfo


class OrderDetailsPage(FletXPage):
    """Orderdetails Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 10,
                vertical = 0,
            ),
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...
        self.order: Optional[OrderInfo] = None

    def on_init(self):
        """Hook called when OrderdetailsPage in initialized"""

        print("OrderdetailsPage is initialized")

    def on_destroy(self):
        """Hook called when OrderdetailsPage will be unmounted."""

        print("OrderdetailsPage is destroyed")

    def build(self)-> Control:
        """Method that build OrderdetailsPage content"""

        # Get Order from navigation
        self.order = self.route_info.data.get('order',None)
        return SafeArea(
            expand = True,
            minimum_padding = 0,
            maintain_bottom_view_padding = False,
            content = Column(
                expand = True,
                alignment = MainAxisAlignment.START,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    # HEADER
                    Row(
                        width = self.width,
                        height = 60,
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment = CrossAxisAlignment.CENTER,
                        controls = [
                            IconButton(
                                icon = Icons.ARROW_BACK,
                                icon_color = Colors.ON_SURFACE,
                                on_click = lambda _: go_back()
                            ),

                            # TITLE
                            Text(
                                f"{self.order.code}",
                                size = 16,
                                weight = FontWeight.W_500
                            ),
                            
                            # PLACE HOLDER
                            Container()
                        ]
                    ),

                    Text("OrderdetailsPage works!", size=24),
                ]
            )
        )