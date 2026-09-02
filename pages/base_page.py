import re

from playwright.sync_api import Page, expect


class BasePage:
    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page

    def open_path(self, path: str = ""):
        self.page.goto(f"{self.BASE_URL}{path}")

    def expect_url_contains(self, value: str):
        expect(self.page).to_have_url(re.compile(rf".*{re.escape(value)}.*"))

