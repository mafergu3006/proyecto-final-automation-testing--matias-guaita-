from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def login(self, username, password):
        logger.info(f"Ingresando usuario: {username}")
        self.type(self.USERNAME, username)
        logger.info("Ingresando contraseña")
        self.type(self.PASSWORD, password)
        logger.info("Haciendo clic en login")
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        msg = self.get_text(self.ERROR_MSG)
        logger.info(f"Mensaje de error obtenido: {msg}")
        return msg
