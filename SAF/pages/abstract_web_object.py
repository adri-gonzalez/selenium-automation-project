from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SAF.pages.page_factory import callable_find_by as find_by
from SAF.pages.pom_meta import PomMeta


class AbstractWebObject(metaclass=PomMeta):
    """
    Base Web Object class to reduce the scope of
    the DOM for section and smaller UI components
    Should not be instantiated directly
    """

    def __init__(self, parent, by, context, element=None):
        """
        Constructor: Create web object to reduce search scope of elements within
        :param parent: web object or web page parent of the web object
        :param by: Locator to initialize cotnext
        :param context: root_element -> element of section for faster search proposes
        :param element: element instance of WebObject
        """
        self.find_by = find_by()
        self.by = by
        self._context = context
        self.parent = parent
        self.found_element = element

    def get_root_element(self):
        self.root_element = self.found_element if self.found_element else self.wait_until_exist()
        return self.root_element

    def wait_until_exist(self, timeout=10):
        if self.found_element:
            return self.found_element
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.presence_of_element_located(self.by))

    def wait_until_not_exist(self, timeout=10):
        wait = WebDriverWait(self._context, timeout)
        return wait.until_not(ec.presence_of_element_located(self.by))

    def wait_until_is_visible(self, timeout=10):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.visibility_of(self.found_element)) if self.found_element else wait.until(
            ec.visibility_of_element_located(self.by))

    def wait_until_is_not_visible(self, timeout=10):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.invisibility_of_element(self.found_element)) if self.found_element else wait.until_not(
            ec.visibility_of_element_located(self.by))

    def exist_child_element(self, by):
        by_constructed = {'strategy': by[0], 'value': by[1]}
        return self.get_root_element().find_elements(by_constructed['strategy'], by_constructed['value']) != []

    def wo_is_clickable(self):
        return self.element().is_displayed() and self.element().is_enabled()

    def element_exist(self):
        self.by_constructed = {'strategy': self.by[0], 'value': self.by[1]}
        return self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value']) != []
