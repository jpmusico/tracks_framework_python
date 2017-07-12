from tracks_framework_python.model.base_test_case import BaseTestCase
from tracks_framework_python.pages.projects import ProjectsPage
from tracks_framework_python.pages.login import LoginPage
import unittest


class SandBox(BaseTestCase):

    def test_test01(self):
        login_page = LoginPage(self._driver)
        projects_page = ProjectsPage(self._driver)

        login_page.navigate()
        login_page.do_login('admin', 'admin')
        projects_page.navigate()
        projects_page.fill_project_name('test')


if __name__ == '__main__':
    unittest.main()
