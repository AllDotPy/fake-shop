"""
fakeShop Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from .pages import (
    CounterPage, NotFoundPage,
    OnboardingPage, LoginPage,
    RegisterPage, MainPage,
    store
)

# Define Fakeshop routes here
routes = [
    {
        'path': '/',
        'component': OnboardingPage,
    },

    # AUTHENTICATION URLS
    {
        'path': '/login',
        'component': LoginPage
    },
    {
        'path': '/register',
        'component': RegisterPage
    },

    # STORE URLS
    {
        'path': '/home',
        'component': MainPage
    },

    # ACCOUNT URLS
    {
        'path': '/profile',
        'component': store.AccountPage
    },

    # UTILITY URLS
    {
        'path': '/counter',
        'component': CounterPage
    },
    {
        'path': '/**',
        'component': NotFoundPage,
    },
]

@register_router
class FakeshopRouter(ModuleRouter):
    """fakeShop Routing Module."""

    name = 'fakeShop'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []