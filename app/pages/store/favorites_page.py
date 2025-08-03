"""
Favorites Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage

# Import your modules here...


class FavoritesPage(FletXPage):
    """Favorites Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...

    def on_init(self):
        """Hook called when FavoritesPage in initialized"""

        print("FavoritesPage is initialized")

    def on_destroy(self):
        """Hook called when FavoritesPage will be unmounted."""

        print("FavoritesPage is destroyed")

    def build(self)-> Control:
        """Method that build FavoritesPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("FavoritesPage works!", size=24),
            ]
        )