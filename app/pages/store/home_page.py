"""
Home Page.

This Page class is generated from a template.
"""

from flet import *
from fletx import FletX
from fletx.core import FletXPage, RxList
from fletx.widgets import Obx
from fletcarousel import (
    BasicAnimatedHorizontalCarousel,
    AutoCycle, HintLine
)

# Import your modules here...
from app.controllers import (
    UsersController, ProductsController,
    CategoriesController, AuthController
)

from app.components import (
    FromTextField, Bannerlist, CategoryList,
    Bannercard, ProductCard
)
from app.models import UserInfo, ProductInfo
from app.utils import BANNERS

# Import your modules here...


class HomePage(FletXPage):
    """Home Page"""

    def __init__(self):
        super().__init__(
            padding = padding.symmetric(
                horizontal = 10,
                vertical = 0,
            ),
            bgcolor = Theme.scaffold_bgcolor,
        )
        # self.width = 300

        # Initializing Reactives
        self.user: UserInfo
        self.banners: RxList = RxList(BANNERS)
        self.categories: RxList = RxList([])

        # Initialize Controllers
        self.usersController: UsersController = FletX.find(
            UsersController, tag = 'users_ctrl'
        )
        self.productsController: ProductsController = FletX.find(
            ProductsController, tag = 'products_ctrl'
        )
        self.categoryController: CategoriesController = FletX.find(
            CategoriesController, tag = 'category_ctrl'
        )

        # Load Data
        self.setup_resources()

    def on_init(self):
        """Hook called when HomePage in initialized"""

        print("HomePage is initialized")

        # Setup cleanups
        self.add_cleanup(
            self.categories.dispose
        )
        self.add_cleanup(
            self.banners.dispose
        )

    def on_destroy(self):
        """Hook called when HomePage will be unmounted."""

        print("HomePage is destroyed")

    def setup_resources(self):
        """Load All needed data"""
        # Get Current User
        self.user = self.categoryController.get_global_context(
            'user'
        )
        # Categories
        self.categories.extend(
            self.categoryController.get_global_context(
                'categories'
            )
        )
        
        # Products

    def build_categories_tabs(self):
        """Build Categories"""

        tabs = Tabs(
            padding = 0,
            selected_index = 1,
            animation_duration = 300,

            # TABS
            tabs = [
                Tab(
                    text = category.name.capitalize(),
                    content = Container(
                        padding = Padding(left = 0, right = 0, top = 10, bottom = 0),
                        content = self.build_category_content(category)
                    )
                )
                for category in self.categories.value
            ]
        )

        return tabs
    
    def build_category_content(self,category:str):
        """Get category news from controller"""

        return GridView(
            spacing = 10,
            padding = padding.symmetric(
                vertical = 5,
                horizontal = 0
            ),
            runs_count = 2,
            run_spacing = 2,
            child_aspect_ratio = .80,
            height = self.height,
            controls = [
                ProductCard(
                    padding = 0,
                    expand = True,
                    border_radius = 10,
                    product = ProductInfo(
                        title = 'My super product',
                        slug = 'super-product',
                        category = self.categories[0],
                        price = 200,
                        images = [
                            'dev1.jpg'
                        ]
                    )
                ) for i in range(16)
            ]
        )

    def build(self)-> Control:
        """Method that build HomePage content"""

        return Column(
            expand = True,
            scroll = ScrollMode.HIDDEN,
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
                        Text(
                            f"Hey, {self.user.first_name if self.user else 'Pythonista'}!",
                            size = 24,
                            weight = FontWeight.W_500
                        ),
                        IconButton(
                            # icon = Icons.NOTIFICATIONS_NONE_OUTLINED,
                            # icon_color = Colors.ON_SURFACE,
                            content = Container(
                                height = 40,
                                width = 40,
                                border_radius= 20,
                                border = Border(
                                    top = BorderSide(
                                        color = Colors.GREY_700,
                                        width = 1
                                    ),
                                    bottom = BorderSide(
                                        color = Colors.GREY_700,
                                        width = 1
                                    ),
                                    left = BorderSide(
                                        color = Colors.GREY_700,
                                        width = 1
                                    ),
                                    right = BorderSide(
                                        color = Colors.GREY_700,
                                        width = 1
                                    )
                                ),

                                content = Icon(
                                    Icons.NOTIFICATIONS_NONE_OUTLINED,
                                    size = 24,
                                    weight = 1,
                                    color = Colors.ON_SURFACE
                                )
                            )
                        )
                    ]
                ),

                # SEARCH BAR
                Container(
                    height = 50,
                    padding = 10,
                    border_radius = 25,
                    bgcolor = Colors.SURFACE,     

                    # Content
                    content = FromTextField(
                        # label = "",
                        hint_text = "Search for products...",
                        # rx_value = self.rx_first_name,
                        expand = True,
                        filled = False,
                        bgcolor = Colors.TRANSPARENT,
                        focused_bgcolor = Colors.TRANSPARENT,

                        # Border
                        border_radius = 0,
                        border = InputBorder.NONE,

                        # Decoration
                        icon = Icons.SEARCH_OUTLINED
                    ),
                ),

                # SPACER
                Container(
                    height = 20
                ),

                # BANNERS
                BasicAnimatedHorizontalCarousel(
                    # page = self.page_instance,
                    auto_cycle = AutoCycle(duration=4),
                    expand = True,
                    width = self.width,
                    padding = 0,
                    animated_switcher = AnimatedSwitcher(
                        content = Control(), 
                        transition = AnimatedSwitcherTransition.FADE, 
                        duration = 500, 
                        reverse_duration = 100,
                    ),
                    hint_lines = HintLine(
                        active_color = Colors.PRIMARY,
                        inactive_color = Colors.ON_PRIMARY_CONTAINER,
                        alignment = MainAxisAlignment.CENTER,
                        max_list_size = 100
                    ),
                    items=[
                        Bannercard(
                            item = i,
                            width = self.width
                        )
                        for i in self.banners.value
                    ],
                ),

                # Container(
                #     height = 150,
                #     width = self.width,
                #     content = Bannerlist(
                #         spacing = 15,
                #         expand = True,
                #         # height = 150,
                #         width = self.width,
                #         horizontal = True,
                #         items = self.banners,
                #     )
                # ),

                # SPACER
                Container(
                    height = 15
                ),

                # CATEGORIES
                Column(
                    width = self.width,
                    controls = [
                        Row(
                            # expand = True,
                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment = CrossAxisAlignment.CENTER,
                            controls = [
                                Text("Categories", size=16, weight=FontWeight.W_500),
                                IconButton(
                                    icon_color=Colors.ON_PRIMARY_CONTAINER,
                                    on_click = lambda e: None,

                                    content = Row(
                                        controls = [
                                            Text("See all", size=14, weight=FontWeight.W_500),
                                            Icon(Icons.ARROW_FORWARD, size=16, color=Colors.ON_PRIMARY_CONTAINER)
                                        ]
                                    )
                                )
                            ]
                        ),

                        # CATEGORY LIST
                        Container(
                            height = 120,
                            width = self.width,
                            # bgcolor = 'red',
                            content = CategoryList(
                                spacing = 20,
                                expand = True,
                                horizontal = True,
                                categories = self.categories
                            )
                        )
                    ]
                ),

                # SPACER
                Container(
                    height = 20
                ),

                # PRODUCTS TABS
                self.build_categories_tabs(),

                Text("MainPage works!", size=24),
            ]
        )