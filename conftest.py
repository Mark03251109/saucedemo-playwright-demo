import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def logged_in_page(login_page: LoginPage):
    return login_page.login_as_standard_user()
