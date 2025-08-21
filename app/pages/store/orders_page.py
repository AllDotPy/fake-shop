"""
Orders Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx import FletX
from fletx.core import FletXPage

# Import your modules here...
from app.controllers import OrderController
from app.components import (
    OrderList
)
from app.models import OrderInfo, OrderStatus

class OrdersPage(FletXPage):
    """Orders Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 10,
                vertical = 0,
            ),
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...
        self.order_controller: OrderController = FletX.find(
            OrderController, tag = 'order_ctrl'
        )

    def on_init(self):
        """Hook called when OrdersPage in initialized"""

        print("OrdersPage is initialized")

    def on_destroy(self):
        """Hook called when OrdersPage will be unmounted."""

        print("OrdersPage is destroyed")

    def load_orders(self):
        """Load all data"""

        # Get Categories
        if not (self.order_controller.objects):
            self.order_controller.all()

    def build_tabs(self):
        """Build Tabs to display Filtered orders."""

        tabs = Tabs(
            padding = 0,
            selected_index = 1,
            animation_duration = 300,

            # TABS
            tabs = [
                Tab(
                    text = state.replace('_',' ').capitalize(),
                    # tab_content = ,
                    content = Container(
                        padding = Padding(left = 0, right = 0, top = 10, bottom = 0),
                        content = # ITEMS
                        Container(
                            expand = True,
                            width = self.width,
                            # bgcolor = 'red',
                            content = OrderList(
                                expand = True,
                                spacing = 10,
                                width = self.width,
                                orders = self.order_controller.objects
                            )
                        ),
                    )
                )
                for state in [
                    OrderStatus.WAITING_FOR_PAYMENT, 
                    OrderStatus.DELIVERING, 
                    OrderStatus.COMPLETED
                ]
            ]
        )

        return tabs

    def build(self)-> Control:
        """Method that build OrdersPage content"""

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
                            f"My Orders",
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
                    content = self.build_tabs()
                    # OrderList(
                    #     expand = True,
                    #     spacing = 10,
                    #     width = self.width,
                    #     orders = self.order_controller.objects
                    # )
                ),
                # Text(f"OrdersPage works!{len(self.order_controller.objects)}", size=24),
            ]
        )