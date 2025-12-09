from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self, product_name):
        btn = (By.XPATH, f"//div[text()='{product_name}']/../../..//button")
        self.click(btn)

    def go_to_cart(self):
        self.click(self.CART_BTN)

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"
