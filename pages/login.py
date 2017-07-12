from selenium import webdriver
from tracks_framework_python.model.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class LoginPage(BasePageObject):

    _locators = {
        'user': (By.ID, 'user_login'),
        'password': (By.ID, 'user_password'),
        'button_login': (By.NAME, 'commit')
    }

    def navigate(self):
        self._driver.get('http://192.168.0.6:8080/projects')

    def do_login(self, user, password):
        user_locator = self._locators['user']
        password_locator = self._locators['password']
        button_login = self._locators['button_login']
        print(user_locator)
        user_input = self._driver.find_element(*user_locator)
        password_input = self._driver.find_element(*password_locator)
        login = self._driver.find_element(*button_login)
        user_input.send_keys(user)
        password_input.send_keys(password)
        login.click()
