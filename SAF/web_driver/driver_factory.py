from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from SAF.utils.constants.driver_type import DriverType
from SAF.utils.constants.platform_type import PlatformType
from SAF.config.settings import Settings
from SAF.config.local import local_capabilities
from SAF.config.cloud import cloud_capabilities
from SAF.web_driver.interceptor.driver_listener import DriverListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from os import environ


class DriverFactory:
    """
    Create a new selenium webdriver or appium driver instance
    based on dot.env configurations. It will allow only a single
    instance of itself to be created.
    """""
    _instance = None

    @staticmethod
    def get_instance() -> object:
        """"
        Method that allows to access to the current
        webdriver instance created, if there is no instance
        created it will be created by accessing this static method.
        """
        if DriverFactory._instance is None:
            DriverFactory()
        return DriverFactory._instance

    @staticmethod
    def dispose_instance():
        try:
            if DriverFactory._instance:
                DriverFactory._instance.delete_all_cookies()
                DriverFactory._instance.quit()
                DriverFactory._instance = None
        except WebDriverException:
            raise WebDriverException("Could not kill webdriver instance")

    def __init__(self):
        if DriverFactory._instance is not None:
            raise Exception("Driver factory already exists")
        else:
            driver = DriverFactory.create_driver()
            DriverFactory._instance = EventFiringWebDriver(driver, DriverListener())

    @staticmethod
    def create_driver():
        """"
        Create webdriver based on DRIVER environment variable
        and PLATFORM environment variable.
        Will return:
        PLATFORM == LOCAL: Local webdriver, take in consideration all
        environment setup when running locally
        PLATFORM == CLOUD: Will run tests on any testing cloud device
        farm configured by environment variables: CLOUD_SERVER, and
        CLOUD_USER: user to be used by the hub in order to authenticate,
        CLOUD_KEY: secret key to authenticate with the CLOUD_USER against
        the CLOUD SERVER.
        """
        driver = Settings.get_driver()
        platform = Settings.get_platform()
        if platform == PlatformType.LOCAL:
            return DriverFactory._create_webdriver_driver(driver)
        elif platform == PlatformType.CLOUD:
            return DriverFactory._create_cloud_driver()
        elif platform == PlatformType.GRID:
            return DriverFactory._create_grid_driver()
        else:
            raise Exception("Non of the platforms were valid")

    @staticmethod
    def _create_webdriver_driver(driver):
        """
        Boiler plate for local webdriver creation(Desktop & Mobile)

        :param driver: driver selected by any engineer.
        e.g. chrome, firefox, android..etc

        :return: function that holds the creation of a local
        webdriver base on driver argument.
        """
        switcher = {
            DriverType.SAFARI: lambda: DriverFactory._create_safari_driver(),
            DriverType.CHROME: lambda: DriverFactory._create_chrome_driver(),
            DriverType.CHROME_HEADLESS: lambda: DriverFactory._create_chrome_driver(True),
            DriverType.FIREFOX: lambda: DriverFactory._create_firefox_driver(),
            DriverType.MICROSOFT_EDGE: lambda: DriverFactory._create_edge_driver(),
            DriverType.PHANTOM_JS: lambda: DriverFactory._create_phantom_js_driver(),
            DriverType.IPAD: lambda: DriverFactory._create_mobile_driver(DriverType.IPAD),
            DriverType.IPHONE: lambda: DriverFactory._create_mobile_driver(DriverType.IPHONE),
            DriverType.ANDROID: lambda: DriverFactory._create_mobile_driver(DriverType.ANDROID),
            DriverType.INTERNET_EXPLORER: lambda: DriverFactory._create_internet_explorer_driver(),
        }
        # Get driver function from switcher dictionary
        func = switcher.get(driver, lambda: Exception("Invalid driver selected"))
        return func()

    @staticmethod
    def _create_mobile_driver(driver):
        """
        Boiler plate to create mobile webdriver

        :param driver: driver selected by any engineer.
        e.g. chrome, firefox, android..etc

        :return: webdriver instance through an appium hub,
        probably hosted in http://127.0.0.1:4723/wd/hub
        """

        if driver == DriverType.ANDROID:
            capabilities = DesiredCapabilities.ANDROID
            capabilities.update(local_capabilities["android"])
        elif driver == DriverType.IPHONE:
            capabilities = DesiredCapabilities.IPHONE
            capabilities.update(local_capabilities["iphone"])
        elif driver == DriverType.IPAD:
            capabilities = DesiredCapabilities.IPAD
            capabilities.update(local_capabilities["ipad"])
        return webdriver.Remote(command_executor=Settings.get_appium_hub(),
                                desired_capabilities=capabilities)

    @staticmethod
    def _create_cloud_driver():
        """
        Boiler plate to create remote webdriver hosted in any
        cloud platform taking the correct webdriver from python
        configuration file cloud.py dictionary

        :return: Cloud webdriver instance
        """
        desired_cap = cloud_capabilities[Settings.get_driver()]
        desired_cap['build'] = Settings.get_build_version()
        return webdriver.Remote(command_executor=Settings.get_cloud_server(),
                                desired_capabilities=desired_cap)

    @staticmethod
    def _create_grid_driver():
        """
        Boiler plate to create remote webdriver hosted in any
        local selenium hub grid taking the correct webdriver from python
        configuration file local.py dictionary

        :return: Cloud webdriver instance
        """
        if Settings.get_driver() == DriverType.CHROME_HEADLESS:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            chrome_options.add_argument('window-size=1300x1080')
            desired_cap = {'browserName': 'chrome', 'javascriptEnabled': True}
            desired_cap.update(chrome_options.to_capabilities())
        elif Settings.get_driver() == DriverType.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--window-size=1680,1050")
            desired_cap = {'browserName': 'firefox'}
            desired_cap.update(firefox_options.to_capabilities())
        else:
            desired_cap = {"browserName": Settings.get_driver()}

        return webdriver.Remote(command_executor=Settings.get_selenium_grid(),
                                desired_capabilities=desired_cap)

    @staticmethod
    def _create_firefox_driver():
        # Return Firefox webdriver instance
        browser_lang = DriverFactory._get_browser_language()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        if browser_lang is not None:
            profile.set_preference("intl.accept_languages", browser_lang)
        return webdriver.Firefox(firefox_profile=profile)

    @staticmethod
    def _create_edge_driver():
        # Return Microsoft Edger chromium webdriver instance
        cap = DesiredCapabilities().EDGE
        cap["platform"] = "ANY"
        # example route_to_driver = "/usr/local/bin/msedgedriver"
        route_to_driver = ''
        return webdriver.Edge(executable_path=route_to_driver, capabilities=cap)

    @staticmethod
    def _create_safari_driver():
        # Return Safari webdriver instance
        return webdriver.Safari()

    @staticmethod
    def _create_phantom_js_driver():
        # Return PhantomJs or GhostDriver webdriver instance
        return webdriver.PhantomJS()

    @staticmethod
    def _create_chrome_driver(headless=False):
        # Return Chrome webdriver instance
        browser_lang = DriverFactory._get_browser_language()
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1300,1080')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
        if browser_lang is not None:
            options.add_experimental_option("prefs", {"intl.accept_languages": browser_lang})
        return webdriver.Chrome(desired_capabilities=options.to_capabilities())

    @staticmethod
    def _create_internet_explorer_driver():
        # Return Internet Explorer 11 webdriver instance
        return webdriver.Ie()

    @staticmethod
    def _get_browser_language():
        return environ.get('BROWSER_LANG', None)
