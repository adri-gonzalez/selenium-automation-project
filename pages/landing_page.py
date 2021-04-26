from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LandingPage(BasePage):
    # navigation
    _call_us_now = by(how=By.CSS_SELECTOR, using="span[class='shop-phone']")
    _contact_us = by(how=By.CSS_SELECTOR, using='#contact-link')
    _sign_in = by(how=By.CSS_SELECTOR, using='.login')

    _home_slider = by(how=By.ID, using='homeslider')
    _home_sliders = by(how=By.CLASS_NAME, using='homeslider-container', multiple=True)

    def wait_until_sliders_visible(self):
        self._home_slider().wait_until_is_visible()
