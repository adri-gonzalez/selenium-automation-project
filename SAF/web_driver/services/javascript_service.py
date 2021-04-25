from SAF.web_driver.driver_factory import DriverFactory


class JavascriptInvokeService:
    def __init__(self):
        self._driver_instance = DriverFactory.get_instance()

    def invoke_script(self, script, *args):
        """
        Execute sync javascript in webdriver
        :param script: String. Javascript code in string format
        :param args: Different objects as arguments in script execution
        :return: Object. Result of javascript code executed
        """
        return self._driver_instance.execute_script(script, args)

    def invoke_async_script(self, script, *args):
        """
        Execute Async javascript code in webdriver
        :param script: String. Javascript code in string format
        :param args: Different objects as arguments in script execution
        :return: Promise. Result of async javascript code executed
        """
        return self._driver_instance.execute_async_script(script, args)
