from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    STANDARD_USER = "standard_user"
    PASSWORD = "secret_sauce"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.open_path()

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_as_standard_user(self):
        self.login(self.STANDARD_USER, self.PASSWORD)

        from pages.inventory_page import InventoryPage
        inventory_page = InventoryPage(self.page)
        inventory_page.expect_loaded()
        return inventory_page

    def expect_error(self, message: str):
        expect(self.error_message).to_contain_text(message)
