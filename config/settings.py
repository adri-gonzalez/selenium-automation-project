import os
from utils.load_env import env_definitions
from utils.constants.platforms import Platforms


class Settings:
    @staticmethod
    def build():
        """
        Build execution configuration based on dot.env
        or behave arguments cli
        :return:
        """
        env_definitions()
        global platform
        platform = Settings._is_platform_valid()

    # JIRA CONFIGURATIONS
    @staticmethod
    def is_jira_enabled():
        try:
            return Settings.get_environment_variable('JIRA_INTEGRATED').lower() in ['true', '1', 't', 'y', 'yes']
        except Exception as e:
            print(f'Exception: {e}')
            return False

    # TEST CONFIGURATIONS
    @staticmethod
    def get_platform():
        return Settings.get_environment_variable('PLATFORM')

    @staticmethod
    def get_app_user():
        return Settings.get_environment_variable('APP_USER'), \
               Settings.get_environment_variable('APP_PASSWORD')

    @staticmethod
    def get_base_url():
        if Settings.get_platform() == Platforms.GRID:
            return Settings.get_environment_variable('CI_URL')
        return 'http://automationpractice.com/index.php'

    @staticmethod
    def _is_platform_valid():
        _platform = os.getenv('PLATFORM').lower()
        if not _platform:
            raise Exception("Platform environment variable is empty")

        _valid_platforms = [Platforms.LOCAL, Platforms.CLOUD, Platforms.GRID]
        if not (_platform in _valid_platforms):
            raise Exception("Current platform is not valid")
        return _platform

    @staticmethod
    def get_environment_variable(env):
        value = os.getenv(env)
        if value:
            return value
        else:
            raise Exception(f"Environment variable {env} is empty")
