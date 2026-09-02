from playwright.sync_api import Page, expect


class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def open_cart(self):
        self.cart_link.click()

    def expect_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))

    def expect_cart_empty(self):
        expect(self.cart_badge).to_have_count(0)
