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

__all__ = [
    'CounterPage',
    'NotFoundPage',
    'OnboardingPage',
    'LoginPage',
    'RegisterPage',
    'MainPage'
]