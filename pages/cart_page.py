from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def expect_loaded(self):
        expect(self.title).to_have_text("Your Cart")

    def expect_product_visible(self, product_name: str):
        expect(self.page.get_by_text(product_name, exact=True)).to_be_visible()

    def checkout(self):
        self.checkout_button.click()

        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.page)
