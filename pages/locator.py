from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocarors():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR,)
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR,)
    BOOK_PRICE = (By.CSS_SELECTOR,)
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR,)