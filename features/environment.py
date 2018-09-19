from behave import *

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def before_scenario(context, scenario):
	options = Options()
	options.add_argument("--headless") # Runs Chrome in headless mode.
	options.add_argument('--no-sandbox') # # Bypass OS security model
	options.add_argument('start-maximized')
	options.add_argument('disable-infobars')
	options.add_argument("--disable-extensions")
	options.add_argument('--disable-gpu')

	context.browser = webdriver.Chrome(chrome_options=options)

def after_scenario(context, scenario):
	context.browser.quit()