from SAF.pages.pom_meta import PomMeta
from SAF.web_driver.services.browser_service import BrowserService
from SAF.web_driver.services.navigation_service import NavigationService
from SAF.web_driver.services.finder_service import FinderService
from SAF.pages.page_factory import callable_find_by as find_by
from SAF.web_driver.driver_factory import DriverFactory
from SAF.pages.events.page_object_event import PageObjectEvent


class AbstractPageObject(metaclass=PomMeta):
    """
    BasePage to implement PageObject model pattern.
    Page Object Model is a design pattern in test automation
    for enhancing test maintenance and reducing code duplication
    Should not be instantiated directly
    """
    _page_object_instantiated = None

    def __init__(self):
        self.finder_service = FinderService()
        self.navigation_service = NavigationService()
        self.find_by = find_by()
        self._driver = DriverFactory.get_instance()
        self.browser_service = BrowserService()

    def on_new_instance(self, page):
        # Trigger page object instantiated event.
        if self._page_object_instantiated is None:
            self._page_object_instantiated = PageObjectEvent()
        self._page_object_instantiated.on_instance += page

    def new_page(self, page_object):
        # Create new PageObject from another PageObject
        if not issubclass(page_object, AbstractPageObject):
            raise Exception("Page object argument is not a valid type", page_object)
        self.on_new_instance(page_object)
        return page_object()

    def new_widget(self, widget_object):
        # Create dynamic widget object in PageObject
        if not issubclass(widget_object, AbstractPageObject):
            raise Exception("Widget object argument is not a valid type", widget_object)
        self.on_new_instance(widget_object)
        return widget_object()
