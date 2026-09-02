PRODUCT_SLUG = "sauce-labs-backpack"


def test_add_product_to_cart(logged_in_page):
    inventory_page = logged_in_page
    inventory_page.add_product(PRODUCT_SLUG)
    inventory_page.header.expect_cart_count(1)


def test_remove_product_from_cart(logged_in_page):
    inventory_page = logged_in_page
    inventory_page.add_product(PRODUCT_SLUG)
    inventory_page.header.expect_cart_count(1)

    inventory_page.remove_product(PRODUCT_SLUG)
    inventory_page.header.expect_cart_empty()
