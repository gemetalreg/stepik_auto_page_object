from .base_page import BasePage
from .locator import BasketPageLocator

class BasketPage(BasePage):

    def is_basket_empty(self):
        empty = self.is_not_element_present(*BasketPageLocator.BASKET_IS_EMPTY)
        assert empty, "Don't empty basket"

    def is_basket_empty_message(self):
        empty = self.is_element_present(*BasketPageLocator.MESSAGE_BASKET_IS_EMPTY)
        assert empty, "No empty basket message"



