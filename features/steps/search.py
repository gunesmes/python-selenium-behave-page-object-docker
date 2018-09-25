from behave import *

import unittest
from selenium import webdriver
from pages.main_page import MainPage



@given(u'I open the main page')
def step_impl(context):
	global page
	page = MainPage(context.browser)
	page.open('/')
	page.check_page_loaded()


@when(u'I search for "{item}"')
def step_impl(context, item):
	page.search_item(item)


@then(u'I should see "{item}" in search result')
def step_impl(context, item):
	assert item in page.get_search_result()
