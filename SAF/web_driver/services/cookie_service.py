from SAF.web_driver.driver_factory import DriverFactory


class CookieService:
    def __init__(self):
        self._driver_instance = DriverFactory.get_instance()

    def get_cookie(self, name):
        # Get cookie by name
        return self._driver_instance.get_cookie(name)

    def get_all_cookies(self):
        # Get all cookies from browser instance
        return self._driver_instance.get_cookies()

    def add_cookie(self, cookie):
        """
        Add cookie to webdriver instance
        :param cookie: Cookie object.
        - cookie_dict: A dictionary object, with required keys - "name" and "value";
            optional keys - "path", "domain", "secure", "expiry"
        :return: void.
        """
        self._driver_instance.add_cookie(cookie)

    def delete_all_cookies(self):
        # Delete all cookies
        self._driver_instance.delete_all_cookies()

    def delete_cookie(self, name):
        # Delete cookie by name
        self._driver_instance.delete_cookie(name)
