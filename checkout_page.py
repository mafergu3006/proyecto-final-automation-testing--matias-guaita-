from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    TITLE = (By.CLASS_NAME, "complete-header")

    def fill_form(self, name, last, zip_code):
        self.type(self.FIRSTNAME, name)
        self.type(self.LASTNAME, last)
        self.type(self.ZIP, zip_code)
        self.click(self.CONTINUE)

    def finish_order(self):
        self.click(self.FINISH)

    def get_confirmation(self):
        return self.get_text(self.TITLE)
