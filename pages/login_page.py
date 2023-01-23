from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "incorrect url"
      
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login_form is absent"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register_form is absent"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.register_form_login)
        login.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators. register_form_password1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators. register_form_password2)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.register_form_button)
        button.click()
        
