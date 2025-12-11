import pytest
import yaml
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from utils.data_reader import read_json

invalid_users = read_json("data/invalid_users.json")

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("user", invalid_users)
def test_login_invalid(driver, user):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["base_url"])

    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])

    error_msg = login_page.get_error_message()

    assert user["error"] in error_msg
