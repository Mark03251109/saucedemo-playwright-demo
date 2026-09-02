PRODUCT_SLUG = "sauce-labs-backpack"
PRODUCT_NAME = "Sauce Labs Backpack"


def test_complete_checkout(logged_in_page):
    inventory_page = logged_in_page
    inventory_page.add_product(PRODUCT_SLUG)

    cart_page = inventory_page.open_cart()
    cart_page.expect_loaded()
    cart_page.expect_product_visible(PRODUCT_NAME)

    checkout_page = cart_page.checkout()
    checkout_page.fill_customer_info("Mark", "Test", "10001")
    checkout_page.finish_order()
    checkout_page.expect_success()
