import os

from web.tests.base_test import BaseTest
from web.pages.login_page import LoginPage


class GoogleLoginTests(BaseTest):
    def setUp(self):
        self.email = os.getenv('gmail_id')
        self.password = os.getenv('gmail_pass')
        self.recovery_email = os.getenv('gmail_recovery_email')

    def test_google_login(self):
        login_page = LoginPage(self.driver)
        login_page.login_using_google(
            self.email, self.password, self.recovery_email)
