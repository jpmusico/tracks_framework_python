from tracks_framework_python.model.base_test_case import BaseTestCase
from tracks_framework_python.pages.projects import ProjectsPage
from tracks_framework_python.pages.login import LoginPage
import unittest


class SandBox(BaseTestCase):

    def test_create_new_project(self):
        login_page = LoginPage(self._driver)
        projects_page = ProjectsPage(self._driver)

        login_page.navigate()
        login_page.do_login('admin', 'admin')
        projects_page.navigate()
        error = projects_page.add_project('new project', 'test note')

        self.assertEqual(error, "None")
        projects_page.delete_project('new project')

    def test_create_new_project_empty_name(self):
        login_page = LoginPage(self._driver)
        projects_page = ProjectsPage(self._driver)

        login_page.navigate()
        login_page.do_login('admin', 'admin')
        projects_page.navigate()
        error = projects_page.add_project('', 'test note')

        self.assertEqual(error, "Name project must have a name")


if __name__ == '__main__':
    unittest.main()
