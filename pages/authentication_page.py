from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthenticationPage(BasePage):
    # create account
    _email_create = by(how=By.CSS_SELECTOR, using='#email_create')
    _create_account = by(how=By.CSS_SELECTOR, using='#SubmitCreate')

    # already registered
    _email_address = by(how=By.CSS_SELECTOR, using='#email')
    _password = by(how=By.CSS_SELECTOR, using='#passwd')
    _forgot_password = by(how=By.CSS_SELECTOR, using='a[title="Recover your forgotten password"]')
    _sign_in = by(how=By.CSS_SELECTOR, using='#SubmitLogin')

    def create_account(self, email):
        self._email_create().send_keys(email)
        self._create_account().click()

    def login(self, email, password):
        self._email_address().send_keys(email)
        self._password().send_keys(password)
        self._sign_in().click()
