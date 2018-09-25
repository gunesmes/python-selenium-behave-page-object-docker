from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
import users
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocatars
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, user):
        self.find_element(*self.locator.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_password(self, user):
        self.find_element(*self.locator.PASSWORD).send_keys(users.get_user(user)["password"])

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text