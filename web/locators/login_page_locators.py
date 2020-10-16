from selenium.webdriver.common.by import By


class LoginPageLocators:
    OFFCIE365_LOGIN_BUTTON = (By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a')
    OFFICE365_LOGIN_FIELD = (By.ID, 'i0116')
    OFFICE365_PASSWORD_FIELD = (By.ID, 'i0118')
    OFFICE365_NEXT_BUTTON = (By.ID, 'idSIButton9')

    GOOGLE_LOGIN_BUTTON = (By.ID, 'gb_70')
    GOOGLE_IDENTIFIER_FIELD = (By.XPATH, '//*[@id ="identifierId"]')
    GOOGLE_IDENTIFIER_NEXT_BUTTON = (By.XPATH, '//*[@id ="identifierNext"]')
    GOOGLE_PASSWORD_FIELD = (
        By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input')
    GOOGLE_PASSWORD_NEXT_BUTTON = (By.XPATH, '//*[@id ="passwordNext"]')
    GOOGLE_ALLOW_BUTTON = (
        By.XPATH, '//*[@id="submit_approve_access"]/div/button')
    GOOGLE_RECOVERY_EMAIL_FIELD = (
        By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')
    GOOGLE_RECOVERY_EMAIL_NEXT_BUTTON = (
        By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
