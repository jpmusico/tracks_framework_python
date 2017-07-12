from selenium import webdriver


class BasePageObject():

    def __init__(self, driver):
        self._driver = driver
        
