from .base_page import BasePage
from .locator import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_btn.click()

    def book_name_in_basket(self, book_name):
        book_name_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        assert book_name.text == book_name_in_msg.text, "Book name don't equal to book name in basket"
        print(f"{book_name} is right")

    def book_price_in_basket(self, book_price):
        book_price_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE)
        assert book_price.text == book_price_in_msg.text, "Book price don't equal to book price in basket"
        print(f"Book price {book_price} is right")

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book_name

    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_sucecess_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message isn't disappiare, but should be"

