"""
Onboarding Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx import FletX
from fletx.core import FletXPage, RxInt, RxBool
from fletx.widgets import Obx
from fletx.navigation import navigate

# Import your modules here...
from app.controllers import CategoriesController
from app.utils import show_snackbar, show_loader


class OnboardingPage(FletXPage):
    """Onboarding Page"""

    def __init__(self):
        self.animation_opacity: RxInt = RxInt(0)
        self.animation_finished: RxBool = RxBool(False)
        
        super().__init__(
            padding = 30,
            bgcolor = Theme.scaffold_bgcolor
        )

        # ...
        self.categoryController: CategoriesController = FletX.find(
            CategoriesController, tag = 'category_ctrl'
        )

    def on_init(self):
        """Hook called when OnboardingPage in initialized"""

        # Watch animation end and change page
        self.watch(
            self.categoryController._is_loading,
            lambda: show_loader(
                controller = self.categoryController,
                page = self.page_instance
            ),
            immediate = True,
        )
        self.watch(
            self.categoryController._error_message,
            lambda: show_snackbar(
                type = 'error',
                page = self.page_instance,
                title = 'Oopss an error occrus!',
                message = self.categoryController._error_message.value
            ) if self.categoryController._error_message.value != '' else None,
            immediate = True
        )

        # Wait one second before starting animation
        import time
        time.sleep(.7)
        self.animation_opacity.value = 1

        # Fetch categories only if needed
        if not self.categoryController.has_context('categories'):
            self.categoryController.set_global_context(
                'categories',
                self.categoryController.all()
            )

    def on_destroy(self):
        """Hook called when OnboardingPage will be unmounted."""

        print("OnboardingPage is destroyed")

    def login_or_home(self):
        """Navigates to login if user is not logged in else get home page."""

        logged_in: bool = self.page_instance.client_storage.get('logged_in') or False
        # navigate to login screen if not logged in
        url = '/login' if not logged_in else '/home'
        navigate(url) 

    def build(self)-> Control:
        """Method that build OnboardingPage content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(      # SPACER
                    expand = True
                ),
                Obx(
                    builder_fn = lambda: Image(
                        src = 'pytg.png',
                        height = 220,
                        fit = ImageFit.COVER,
                        animate_opacity = 500,
                        opacity = self.animation_opacity.value,
                    ),
                ),
                Container(      # SPACER
                    expand = True
                ),
                Obx(
                    builder_fn = lambda: Text(
                        "Welcome to the Python Togo Store", 
                        size = 16,
                        animate_opacity = 500,
                        opacity = self.animation_opacity.value,
                        on_animation_end = lambda _: self.animation_finished.toggle()
                    ),
                ),
                Container(      # SPACER
                    height = 20
                ),
                Obx(
                    builder_fn = lambda: FilledButton(
                        "Continue",
                        width = self.width,
                        height = 50,
                        on_click = lambda e: navigate('/login'),
                        opacity = self.animation_opacity.value,
                        style = ButtonStyle(
                            text_style = TextStyle(
                                size = 16,
                                weight = FontWeight.BOLD
                            )
                        )
                    ),
                ),
                Container(      # SPACER
                    height = 10
                ),
            ]
        )