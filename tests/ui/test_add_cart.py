import pytest
import yaml
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["base_url"])

    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    assert "cart" in driver.current_url
