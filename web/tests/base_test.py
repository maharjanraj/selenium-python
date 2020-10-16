import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from web.libs.router import Router


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 30)
        cls.driver.maximize_window()
        cls.router = Router(cls.driver, os.getenv('host'))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        if hasattr(cls, 'driver'):
            cls.driver.quit()
