import pytest
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
])
def test_login(driver, username, password, expected):
    logger.info("Abriendo página de login")
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected:
        # login exitoso
        assert "inventory" in driver.current_url
        logger.info(f"Login exitoso para usuario {username}")
    else:
        # login fallido
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg.lower()
        logger.warning(f"Login fallido para usuario {username} con mensaje: {error_msg}")
