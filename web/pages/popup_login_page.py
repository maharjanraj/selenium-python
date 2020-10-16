from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from web.pages.base_page import BasePage
from web.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def login_using_google(self, gmail_id, password, recovery_email):
        # store main page window handle for switching back
        main_page_handle = self.driver.current_window_handle

        # google login button
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_LOGIN_BUTTON).click()

        # wait for popup to open
        sleep(3)

        # find google login popup window handle
        login_page_handle = ''
        for handle in self.driver.window_handles:
            if handle != main_page_handle:
                login_page_handle = handle

        # switch driver handle to google login popup window
        self.driver.switch_to.window(login_page_handle)

        # enter email and password
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_IDENTIFIER_FIELD).send_keys(gmail_id)
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_IDENTIFIER_NEXT_BUTTON).click()
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_PASSWORD_NEXT_BUTTON).click()

        # recovery email
        try:
            self.driver.find_element(
                *LoginPageLocators.GOOGLE_RECOVERY_EMAIL_FIELD).send_keys(recovery_email)
            self.driver.find_element(
                *LoginPageLocators.GOOGLE_RECOVERY_EMAIL_NEXT_BUTTON).click()
        except NoSuchElementException:
            pass

        # allow permissions
        self.driver.find_element(
            *LoginPageLocators.GOOGLE_ALLOW_BUTTON).click()

        # wait for login success
        sleep(5)

        # switch back to main window
        self.driver.switch_to.window(main_page_handle)

    def login_using_office365(self, email, password):
        # store main page window handle for switching back
        main_page_handle = self.driver.current_window_handle

        # google login button
        self.driver.find_element(
            *LoginPageLocators.OFFCIE365_LOGIN_BUTTON).click()

        # wait for popup to open
        sleep(3)

        # find google login popup window handle
        for handle in self.driver.window_handles:
            if handle != main_page_handle:
                login_page_handle = handle

        # switch driver handle to google login popup window
        self.driver.switch_to.window(login_page_handle)

        # enter email and password
        self.wait.until(EC.element_to_be_clickable(
            LoginPageLocators.OFFICE365_LOGIN_FIELD)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(
            LoginPageLocators.OFFICE365_NEXT_BUTTON)).click()

        self.wait.until(EC.element_to_be_clickable(
            LoginPageLocators.OFFICE365_PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(
            LoginPageLocators.OFFICE365_NEXT_BUTTON)).click()

        # wait for login success
        sleep(5)

        # switch back to main window
        self.driver.switch_to.window(main_page_handle)
