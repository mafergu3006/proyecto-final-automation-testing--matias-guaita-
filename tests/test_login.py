import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.data_loader import load_json

credentials = load_json("data/login_data.json")

@pytest.mark.parametrize("data", credentials[:2])  # Solo usuarios válidos
def test_login_success(driver, data):
    login = LoginPage(driver)
    login.login(data["username"], data["password"])

    products = ProductsPage(driver)
    assert products.is_loaded()
