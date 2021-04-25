from SAF.web_driver.driver_factory import DriverFactory
from SAF.utils.constants.screen_sizes import ScreenSizes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoAlertPresentException


class BrowserService:
    """
    Browser service class will encapsulate webdriver behaviour
    in order to handle all related window/browser events
    """

    def __init__(self):
        self._driver_instance = DriverFactory.get_instance()

    def get_source_string(self):
        # Gets the source of the current page
        return self._driver_instance.page_source

    def switch_to_latest_tab(self):
        """
        Take all windows in webdriver instance
        and switch to the latest one
        :return: return the webdriver session in the
        latest window of it's instance
        """
        windows = self._driver_instance.window_handles
        latest_window = windows[len(windows) - 1]
        return self._driver_instance.switch_to.window(latest_window)

    def switch_to_alert(self):
        # Switch to javascript pop-up alert
        return self._driver_instance.switch_to.alert

    def dismiss_alert(self, timeout=30):
        """
        Search for javascript pop-up alert for a
        specific period of time. Switch to the alert if
        it exists and dismiss it.
        :param timeout: specific time to wait for
        alert to appear on the UI.
        :return: void.
        """
        if not self.is_alert_preset(timeout):
            return
        self.switch_to_alert().dismiss()

    def is_alert_present(self, timeout=30):
        """
        Wait for javascript pop-up to be visible
        in the UI
        :param timeout: Specific period of time to wait
        for javascript pop-up.
        :return: boolean.
        """
        wait = WebDriverWait(self._driver_instance, timeout)
        try:
            wait.until(ec.alert_is_present)
            return True
        except NoAlertPresentException:
            return False

    def refresh(self):
        # Refresh webdriver instance
        self._driver_instance.refresh()

    def close_driver(self):
        # Close webdriver instance
        self._driver_instance.close()

    def quit_driver(self):
        # Quit webdriver instance
        self._driver_instance.quit()

    def resize_browser(self, size):
        """
        Resize browser window for web responsive implementations
        :param size: Dictionary base on real devices sizes
        :return: void.
        """
        if not isinstance(size, ScreenSizes):
            raise Exception("Screen size selected is not a valid type")
        width = size[0]
        height = size[1]
        self._driver_instance.set_window_size(width, height)

    def switch_to_iframe(self, iframe):
        self._driver_instance.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self._driver_instance.switch_to_default_content()

    def override_location(self, params):
        self._driver_instance.execute_cdp_cmd("Page.setGeolocationOverride", params)
