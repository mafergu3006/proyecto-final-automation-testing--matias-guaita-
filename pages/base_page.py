from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        logger.info(f"Haciendo clic en {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        logger.info(f"Escribiendo '{text}' en {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        logger.info(f"Obteniendo texto de {locator}: '{text}'")
        return text
