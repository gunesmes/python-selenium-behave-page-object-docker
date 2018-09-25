from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from support.users import users
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class MainPage(BasePage):
  # Web elements on Main Page
  LOGO          = (By.ID, 'nav-logo')
  ACCOUNT       = (By.ID, 'nav-link-yourAccount')
  SIGNUP        = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
  LOGIN         = (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.ID, 's-results-list-atf')

  def __init__(self, driver):
    super().__init__(driver)  # Python3 version

  def check_page_loaded(self):
    return True if self.find_element(*self.LOGO) else False

  def search_item(self, item):
    self.find_element(*self.SEARCH).send_keys(item)
    self.find_element(*self.SEARCH).send_keys(Keys.ENTER)
 
  def get_search_result(self):
    return self.find_element(*self.SEARCH_LIST).text
      
  def click_sign_up_button(self):
    self.hover(*self.ACCOUNT)
    self.find_element(*self.SIGNUP).click()
    return SignUpPage(self.driver)

  def click_sign_in_button(self):
    self.hover(*self.ACCOUNT)
    self.find_element(*self.LOGIN).click()
    return LoginPage(self.driver)