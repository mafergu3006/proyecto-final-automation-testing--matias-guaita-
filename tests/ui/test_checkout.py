from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product("Sauce Labs Bike Light")
    products.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Juan", "Perez", "12345")
    checkout.finish_order()

    assert checkout.get_confirmation() == "Thank you for your order!"
