import os


class Settings:
    @staticmethod
    def get_driver():
        return os.getenv('DRIVER')

    @staticmethod
    def get_appium_hub():
        return os.getenv('APPIUM_HUB')

    @staticmethod
    def get_selenium_grid():
        return os.getenv('SELENIUM_GRID')

    @staticmethod
    def get_cloud_server():
        return os.getenv('CLOUD_HUB')

    @staticmethod
    def get_cloud_key():
        return os.getenv('CLOUD_KEY')

    @staticmethod
    def get_build_version():
        return os.getenv('BUILD_VERSION')

    @staticmethod
    def get_platform():
        return os.getenv('PLATFORM')

    @staticmethod
    def get_debug_mode():
        return os.getenv('DEBUG_MODE')
