"""
Main Controller.

This Page class is generated from a template.
"""

import gc
from flet import *
from fletx import FletX
from typing import List, Optional
from fletx.core import FletXPage
from fletx.decorators import obx
from fletx.widgets import Obx

# Import your modules here...
from .store import (
    HomePage, FavoritesPage,
    ShoppingCartPage, AccountPage,
    OrdersPage
)
from app.controllers import AuthController


class MainPage(FletXPage):
    """Main Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 0,
                vertical = 0
            ),
            bgcolor = Theme.scaffold_bgcolor
        )

        # Inject Auth COntroller
        self.auth_controller: AuthController = FletX.find(
            AuthController, tag = 'auth_ctrl'
        )

        self.current_index = self.auth_controller.create_rx_int(0)

        # Store current page content
        self.page_content: Optional[FletXPage] = None

        # Build first content
        self.change_content(
            self.current_index.value
        )

    def on_init(self):
        """Hook called when MainPage in initialized"""

        print("MainPage is initialized")
        # Build NavigationBar
        self.build_navigation()

        # watch index fo rebuild the page content
        self.watch(
            self.current_index,
            lambda: self.change_content(
                self.current_index.value,
                update = True
            )
        )
        
    def on_destroy(self):
        """Hook called when MainPage will be unmounted."""

        print("MainPage is destroyed")

    def change_content(self,index: int = 0, update: bool = False):
        """Change page content"""

        pages: List[FletXPage] = [
            HomePage,
            FavoritesPage,
            ShoppingCartPage,
            OrdersPage,
            AccountPage,
        ]

        # Dispose existing page content
        if self.page_content:
            self.page_content.will_unmount()
            self.page_content.dispose()
            # gc.collect()# self.page_content

        self.page_content = pages[index]()
        self.page_content._build_page()

        if update:
            # self._build_page()
            self.content.content = self.page_content
            self.content.update()

        # return page_content

    def change_index(self, new_idx:int):
        """Change current Page Index"""
        self.current_index.value = new_idx

    def build_navigation(self):
        """Method that build MainPage navigation"""

        self.page_instance.views[-1].navigation_bar = NavigationBar(
            selected_index = 0,
            elevation = 50,
            bgcolor = Colors.SURFACE,
            indicator_color = Colors.PRIMARY,
            width = self.width,
            height = 80,
            on_change = lambda e: self.change_index(int(e.data)), 
            destinations = [
                NavigationBarDestination(
                    icon = Icons.STORE_MALL_DIRECTORY_OUTLINED,
                    selected_icon = Icons.STORE_MALL_DIRECTORY,
                    label = "Store"
                ),
                NavigationBarDestination(
                    icon = Icons.FAVORITE_BORDER_OUTLINED,
                    selected_icon = Icons.FAVORITE,
                    label = "Favorites"
                ),
                NavigationBarDestination(
                    icon = Icons.SHOPPING_CART_OUTLINED,
                    selected_icon = Icons.SHOPPING_CART,
                    label = "Cart"
                ),
                NavigationBarDestination(
                    icon = Icons.SHOPPING_BAG_OUTLINED,
                    selected_icon = Icons.SHOPPING_BAG,
                    label = "Orders"
                ),
                NavigationBarDestination(
                    icon = Icons.PERSON_OUTLINE,
                    selected_icon = Icons.PERSON,
                    label = "Profile"
                )
            ]
        )
        self.page_instance.update()
    
    def build(self)-> Control:
        """Method that build MainPage content"""
        return SafeArea(
            expand = True,
            minimum_padding = 0,
            maintain_bottom_view_padding = False,
            content = self.page_content
        )
