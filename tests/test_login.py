from pages.login_page import LoginPage


def test_valid_login(login_page: LoginPage):
    inventory_page = login_page.login_as_standard_user()
    inventory_page.expect_loaded()


def test_invalid_login(login_page: LoginPage):
    login_page.login("invalid_user", "wrong_password")
    login_page.expect_error("Username and password do not match")
