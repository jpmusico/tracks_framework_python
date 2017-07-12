import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self._driver = webdriver.Firefox()

    def tearDown(self):
        self._driver.quit()
