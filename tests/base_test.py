import unittest

import pytest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    page_class = None
    page_url = None

    def setUp(self, browser='chrome'):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'safari':
            self.driver = webdriver.Safari()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Invalid browser name")

        self.driver.maximize_window()
        if self.page_url is not None:
            self.driver.get(self.page_url)
        self.page = self.page_class(self.driver)

    def tearDown(self):
        self.driver.quit()
