"""
Fakeshop Application Pages module.

This module contains the application Pages.
Version: 0.1.0
"""

from .counter import CounterPage
from .not_found import NotFoundPage
from .onboarding_page import OnboardingPage
from .auth.login_page import LoginPage
from .auth.register_page import RegisterPage
from .main_page import MainPage
from .shared.producrdetails_page import ProducrDetailsPage
from .shared.notifications_page import NotificationsPage
from .shared.search_page import SearchPage

__all__ = [
    'CounterPage',
    'NotFoundPage',
    'OnboardingPage',
    'LoginPage',
    'RegisterPage',
    'MainPage',
    'ProducrDetailsPage',
    'NotificationsPage',
    'SearchPage'
]