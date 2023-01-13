from .base_page import BasePage
from .locator import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_btn.click()