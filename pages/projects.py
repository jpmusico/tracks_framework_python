from tracks_framework_python.model.base_page_object import BasePageObject
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class ProjectsPage(BasePageObject):

    input_new_name = (By.ID, 'project_name')
    input_new_description = (By.ID, 'project_description')

    button_new_add = (By.ID, 'project_new_project_submit')

    text_error_information = (By.ID, 'errorExplanation')

    def navigate(self):
        self._driver.get(self._baseUrl + '/projects')

    def fill_project_name(self, name):
        new_name = self._driver.find_element(*self.input_new_name)
        new_name.send_keys(name)

    def fill_description(self, description):
        new_description = self._driver.find_element(*self.input_new_description)
        new_description.send_keys(description)

    def add_project(self, name, description):
        self.fill_project_name(name)
        self.fill_description(description)
        button_add = self._driver.find_element(*self.button_new_add)
        button_add.click()
        return self.get_error()

    def delete_project(self, name, confirm=True):
        try:
            button_delete = self._driver.find_element_by_xpath(".//*[@id[contains(.,'container_project_')] and .//a[text()='"+name+"']]//a[@id[contains(.,'delete_project')]]")
        except NoSuchElementException:
            return 'Project Not Found'
        button_delete.click()
        try:
            self._driver.switch_to_alert().accept()
        except NoAlertPresentException:
            return "Confirmation alert not displayed"


    def get_error(self):
        try:
            text_error = self._driver.find_element(*self.text_error_information)
        except NoSuchElementException:
            return 'None'
        return text_error.text
