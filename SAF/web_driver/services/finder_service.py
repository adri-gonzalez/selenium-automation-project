from SAF.web_driver.driver_factory import DriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException


class FinderService:
    """
    Find single or multiple elements dynamically in
    DOM under expected conditions
    """

    def __init__(self, context=None):
        self._driver_instance = DriverFactory.get_instance() if context is None else context

    def get_element(self, selector, wait_located=True, timeout=30):
        """
        Get WebElement from DOM base on any locator
        :param selector: locator to search WebElement
        :param wait_located: boolean. If true will wait for element
        to be on DOM
        :param timeout: Specific period of time to wait for element
        to be in the HTML
        :return: WebElement.
        """
        self._is_selector_valid(selector)
        selector_type = selector[0]
        selector_value = selector[1]

        try:
            if wait_located:
                return WebDriverWait(self._driver_instance, timeout).until(
                    ec.presence_of_element_located(selector))
            else:
                return self._driver_instance.find_element(selector_type, selector_value)
        except NoSuchElementException:
            raise NoSuchElementException(f"Could not find element by the locator: {str(selector)}")

    def get_elements(self, selector, wait_located=True, timeout=30):
        """
        Get array of WebElements that match with the locator specified
        in the DOM
        :param selector: locator to search WebElement
        :param wait_located: boolean. If true will wait for
        all elements to be on DOM
        :param timeout: Specific period of time to wait for element
        to be in the HTML
        :return: Array of WebElements
        """
        self._is_selector_valid(selector)
        selector_type = selector[0]
        selector_value = selector[1]

        try:
            if wait_located:
                return WebDriverWait(self._driver_instance, timeout).until(
                    ec.presence_of_all_elements_located(selector))
            else:
                return self._driver_instance.find_elements(selector_type, selector_value)
        except NoSuchElementException:
            raise NoSuchElementException(f"Could not find element by the locator: {str(selector)}")

    @staticmethod
    def _is_selector_valid(selector):
        selector_type = selector[0]
        selector_value = selector[1]

        _selector_array = [By.ID, By.CSS_SELECTOR, By.CLASS_NAME, By.LINK_TEXT,
                           By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME, By.XPATH]

        if not type(selector) is tuple:
            raise InvalidSelectorException("Current locator is not a valid type")

        if not any(selector_type in s for s in _selector_array):
            raise InvalidSelectorException("Current locator is not a valid type")

        if selector_value is None:
            raise InvalidSelectorException("Current locator is not a valid type")
