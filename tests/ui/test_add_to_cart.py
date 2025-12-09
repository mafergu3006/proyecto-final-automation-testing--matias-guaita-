from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product("Sauce Labs Backpack")
    products.go_to_cart()

    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in driver.page_source

