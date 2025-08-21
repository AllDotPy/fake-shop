"""
Checkout Controller.

This Page class is generated from a template.
"""

from flet import *
from typing import Optional
import flet_webview as ftwv
from fletx.core import FletXPage
from fletx.navigation import go_back

# Import your modules here...
from app.models import OrderInfo
from app.utils import show_snackbar


class CheckoutPage(FletXPage):
    """Checkout Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 0,
                vertical = 0,
            ),
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...
        self.order: Optional[OrderInfo] = None

    def on_init(self):
        """Hook called when CheckoutPage in initialized"""

        print("CheckoutPage is initialized")
        show_snackbar(
            self.page_instance, 
            title = "Order Successful", 
            message = "You have successfully made Order.", 
            type = 'success'
        )

    def on_destroy(self):
        """Hook called when CheckoutPage will be unmounted."""

        print("CheckoutPage is destroyed")

    def build(self)-> Control:
        """Method that build CheckoutPage content"""

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
                                f"Checkout",
                                size = 16,
                                weight = FontWeight.W_500
                            ),

                            Container(
                                width = 40
                            )
                        ]
                    ),
                    ftwv.WebView(
                        url = f"{self.order}",
                        on_page_started = lambda _: print("Page started"),
                        on_page_ended = lambda _: print("Page ended"),
                        on_web_resource_error = lambda e: print("Page error:", e.data),
                        expand = True,
                        enable_javascript = True,
                    )
                ]
            )
        )