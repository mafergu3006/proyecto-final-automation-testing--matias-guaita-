from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn_inventory")
    CART_ICON = (By.ID, "shopping_cart_container")

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)
