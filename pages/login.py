from tracks_framework_python.model.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class LoginPage(BasePageObject):

    input_user = (By.ID, 'user_login')
    input_password = (By.ID, 'user_password')
    button_login = (By.NAME, 'commit')

    def navigate(self):
        self._driver.get(self._baseUrl + '/login')

    def do_login(self, user, password):
        user_input = self._driver.find_element(*self.input_user)
        password_input = self._driver.find_element(*self.input_password)
        login = self._driver.find_element(*self.button_login)
        user_input.send_keys(user)
        password_input.send_keys(password)
        login.click()
