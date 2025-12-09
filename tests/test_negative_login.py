from pages.login_page import LoginPage

def test_login_invalid(driver):
    login = LoginPage(driver)
    login.login("invalid", "wrong")

    assert "Username and password" in login.get_error_message()
