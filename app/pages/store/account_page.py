"""
Account Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage

# Import your modules here...


class AccountPage(FletXPage):
    """Account Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...

    def on_init(self):
        """Hook called when AccountPage in initialized"""

        print("AccountPage is initialized")

    def on_destroy(self):
        """Hook called when AccountPage will be unmounted."""

        print("AccountPage is destroyed")

    def build(self)-> Control:
        """Method that build AccountPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Text("AccountPage works!", size=24),
            ]
        )