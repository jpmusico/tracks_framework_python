from selenium import webdriver
from tracks_framework_python.model.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class ProjectsPage(BasePageObject):

    _locators = {
        'new_project_name_input': (By.ID, 'project_name')
    }

    def navigate(self):
        self._driver.get('http://192.168.0.6:8080/projects')

    def fill_project_name(self, name):
        locator = self._locators['new_project_name_input']
        project_name = self._driver.find_element(*locator)
        project_name.send_keys(name)
