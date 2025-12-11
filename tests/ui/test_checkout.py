import pytest
import yaml
from utils.driver_factory import DriverFactory
from utils.data_reader import read_json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

checkout_data = read_json("data/checkout_data.json")

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("data", checkout_data)
def test_checkout_flow(driver, data):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["base_url"])

    # login
    LoginPage(driver).login("standard_user", "secret_sauce")

    # add product
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # go to checkout
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    # fill checkout form
    checkout = CheckoutPage(driver)
    checkout.fill_form(data["first_name"], data["last_name"], data["zip"])
    checkout.finish_purchase()

    assert checkout.purchase_successful()
