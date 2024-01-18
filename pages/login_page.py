from .locators import LoginPageLocators
from .base_page import BasePage
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):

        login = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        psw = self.browser.find_element(*LoginPageLocators.REG_PASS)
        psw_conf = self.browser.find_element(*LoginPageLocators.REG_PASSCONF)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)

        login.send_keys(email)
        psw.send_keys(password)
        psw_conf.send_keys(password)
        reg_btn.click()
