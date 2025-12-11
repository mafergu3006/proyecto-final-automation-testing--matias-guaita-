from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form(self, first, last, zip_code):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_purchase(self):
        self.click(self.FINISH_BTN)

    def purchase_successful(self):
        return "Thank you" in self.find(self.CONFIRM_MSG).text
