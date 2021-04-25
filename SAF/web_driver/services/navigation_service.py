from SAF.web_driver.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NavigationService:
    """
    Navigation service class will encapsulate webdriver behaviour
    in order to handle all related navigation events
    """

    def __init__(self):
        self._driver_instance = DriverFactory.get_instance()

    def get_current_url(self):
        # Returns current webdriver url
        return self._driver_instance.current_url

    def get_current_title(self):
        # Returns current webdriver title
        return self._driver_instance.title

    def navigate_to(self, url):
        # Navigate to url
        self._driver_instance.get(url)

    def navigate_back(self):
        # Navigate back in browser history
        self._driver_instance.back()

    def navigate_forward(self):
        # Navigate forward in browser history
        self._driver_instance.forward()

    def wait_for_url(self, url, timeout=30):
        """
        Wait for webdriver url to be exactly as the
        argument url
        :param url: url to be compared
        :param timeout: Specific period of time to wait for url
        to match
        :return: void.
        """
        wait = WebDriverWait(self._driver_instance, timeout)
        wait.until(ec.url_to_be(url))

    def wait_for_partial_url(self, url, timeout=30):
        """
        Wait for webdriver url to be partially equal as the
        argument url
        :param url: url to be compared
        :param timeout: Specific period of time to wait for url
        to match
        :return: void.
        """
        wait = WebDriverWait(self._driver_instance, timeout)
        wait.until(ec.url_contains(url))

    def wait_for_ajax(self, timeout=30):
        """
        Wait for all ajax request in webdriver to finish
        :param timeout: Specific period of time to wait for ajax
        request to finish loading
        :return: void.
        """
        active_ajax_javascript = "return typeof document != 'undefined' && document.readyState == 'complete' && typeof $ != 'undefined';"
        wait = WebDriverWait(self._driver_instance, timeout)
        wait.until(lambda _driver_instance: _driver_instance.execute_script(active_ajax_javascript) == 0)

    def wait_until_document_ready(self, time_out=30):
        """
        Wait for HTML document to be ready
        :param time_out: Specific period of time to wait for document
        to be ready
        :return: void.
        """
        wait = WebDriverWait(self._driver_instance, time_out)
        wait.until(lambda _driver_instance: _driver_instance.execute_script("return document.readyState") == "complete")

    def navigate_to_page(self, url, page_object):
        """
        Navigate to Url and create a page object
        :param url: url to navigate
        :param page_object: Landing page where driver will start
        :return: page_object() instance
        """
        self._driver_instance.get(url)
        return page_object()

    def relaunch(self, page_object=None, initial_url=None, clear_cookies=True):
        """
        Closes the browser and launches it again.
        :param page_object: Page Object of the expected web page to navigate to
        :param initial_url: URL to navigate to after relaunch.
        :param clear_cookies: Whether or not to clear browser cookies during relaunch
        :return: Instance of the indicated Page Objec
        """
        if self._driver_instance.window_handles is None:
            return

        if initial_url is None:
            initial_url = self._driver_instance.current_url

        if clear_cookies:
            self._driver_instance.delete_all_cookies()

        self.navigate_to(initial_url)
        return page_object()
