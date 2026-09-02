from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.header_component import HeaderComponent


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.header = HeaderComponent(page)

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")

    def add_product(self, product_slug: str):
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def remove_product(self, product_slug: str):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()

    def open_cart(self):
        self.header.open_cart()

        from pages.cart_page import CartPage
        return CartPage(self.page)
