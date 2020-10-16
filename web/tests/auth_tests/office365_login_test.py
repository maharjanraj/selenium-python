import os

from web.tests.base_test import BaseTest
from web.pages.login_page import LoginPage


class Office365LoginTests(BaseTest):
    def setUp(self):
        self.email = os.getenv("office365_id")
        self.password = os.getenv("office365_pass")

    def test_office365_login(self):
        self.driver.get('https://hotmail.com')
        login_page = LoginPage(self.driver)
        login_page.login_using_office365(self.email, self.password)