from pages.base_page import BasePage


def initial_page(url, page):
    """
    Create initial page in tests to avoid page object
    construction in steps definition
    :param url: Url to be navigated
    :param page: Landing page according to the page parameter
    :return: Page object model instance
    """
    if not issubclass(page, BasePage):
        raise Exception("Current argument is not instance of AbstractPageObject")
    _initial_page = page()
    _initial_page.navigation_service.navigate_to(url)
    _initial_page.wait_until_page_finish_load()
    return _initial_page


def create_page(page):
    if not issubclass(page, BasePage):
        raise Exception("Current argument is not instance of AbstractPageObject")
    _initial_page = page()
    return _initial_page
