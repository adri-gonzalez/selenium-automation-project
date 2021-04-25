import time
from SAF.config.settings import Settings
from selenium.webdriver.support.events import AbstractEventListener


class DriverListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigating to ", url)

    def after_navigate_to(self, url, driver):
        print("After navigating to ", url)

    def before_navigate_back(self, driver):
        print("before navigating back ", driver.current_url)

    def after_navigate_back(self, driver):
        print("After navigating back ", driver.current_url)

    def before_navigate_forward(self, driver):
        print("before navigating forward ", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After navigating forward ", driver.current_url)

    def before_find(self, by, value, driver):
        print("before find", str(by), str(value))

    def after_find(self, by, value, driver):
        print("after find", str(by), str(value))

    def before_click(self, element, driver):
        self._highlight(element, driver)
        print("before click on element", element)

    def after_click(self, element, driver):
        print("after click on element", element)

    def before_change_value_of(self, element, driver):
        print("before change value of element", element)

    def after_change_value_of(self, element, driver):
        print("after change value of element", element)

    def before_execute_script(self, script, driver):
        print("before execute script:", script)

    def after_execute_script(self, script, driver):
        print("after execute script:", script)

    def before_close(self, driver):
        print("before closing driver")

    def after_close(self, driver):
        print("after closing driver")

    def before_quit(self, driver):
        print("before quit driver")

    def after_quit(self, driver):
        print("after quit driver")

    def on_exception(self, exception, driver):
        print("on_exception")
        print(f"{exception}")

    def _highlight(self, element, driver, duration=1):
        """
        This method highlight the element with a red border for a sleep time and after that
        go back to the original style
        :param element -> selenium web element
        :param driver -> selenium driver base
        :param duration -> time of highlight by default 1 , int
        :return void
        """
        # check if config is in debug mode is not go back and do nothing
        if not bool(Settings.get_debug_mode()):
            return

        # store original style so it can be reset later
        original_style = element.get_attribute("style")

        # style element with red border
        driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", element, "style",
                              "border: 2px solid red; border-style: dashed;")

        # keep element highlighted for automation spell and then revert
        if duration > 0:
            time.sleep(duration)
            driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", element, "style",
                                  original_style)
