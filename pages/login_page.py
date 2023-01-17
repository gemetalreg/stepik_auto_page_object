from .base_page import BasePage
from .locator import LoginPageLocarors
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        email_input.send_keys(email)

        pass1_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        pass1_input.send_keys(password)
        pass2_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        pass2_input.send_keys(password)

        register_bth = self.browser.find_element(By.CSS_SELECTOR, "button[name='registration_submit']")
        register_bth.click()



    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocarors.LOGIN_FORM_LINK), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocarors.REGISTER_FORM_LINK), "Register form is not presented"
