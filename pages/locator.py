from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocarors():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")