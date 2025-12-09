from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_navigation_products(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    assert products.is_loaded()
