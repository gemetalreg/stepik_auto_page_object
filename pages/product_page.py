from .base_page import BasePage
from .locator import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_btn.click()

    def book_name_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        assert book_name.text == book_name_in_msg.text, "Book name don't equal to book name in basket"
        print(f"{book_name} is right")

    def book_price_in_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE)
        print(book_price, book_price_in_msg)
        assert book_price.text == book_price_in_msg.text, "Book price don't equal to book price in basket"
        print(f"Book price {book_price} is right")