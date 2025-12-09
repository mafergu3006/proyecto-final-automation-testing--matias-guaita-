from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from datetime import datetime

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text



    def screenshot(self, name="screenshot"):
        """Guarda un screenshot en caso de fallo con fecha y hora"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder = os.path.join("reports", "screenshots")
        os.makedirs(folder, exist_ok=True)
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(folder, filename)
        self.driver.save_screenshot(path)
        return path
