import abc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SAF.web_driver.services.finder_service import FinderService
from SAF.web_driver.driver_factory import DriverFactory


class Element(metaclass=abc.ABCMeta):
    def __init__(self, parent, context):
        """
        Base element constructor to be override be derived classes
        :param parent: web object or web page parent of the web object
        :param context: root_element -> element of section for faster search proposes if is null is _driver
        """
        self.parent = parent
        self._context = context
        self.find_by = FinderService(context)

    @abc.abstractmethod
    def element(self):
        pass

    @abc.abstractmethod
    def wait_until_is_visible(self, timeout=20):
        pass

    def send_keys(self, value, timeout=20, existence=False):
        element = self.wait_until_exist(timeout) if existence else self.wait_until_is_visible(timeout)
        if element is not None:
            element.send_keys(value)

    def element_is_visible(self):
        return self.element().is_displayed()

    def element_is_clickable(self):
        return self.element().is_displayed() and self.element().is_enabled()

    def get_text(self, text_sanitize=True, timeout=10):
        element = self.wait_until_is_visible(timeout)
        return element.text.lower().strip() if text_sanitize else element.text

    def clear_text_by_js(self):
        self.send_text_js("")

    def send_text_js(self, text, timeout=20):
        element = self.wait_until_is_visible(timeout)
        DriverFactory.get_instance().execute_script('arguments[0].value=arguments[1];', element.wrapped_element,
                                                    text)

    def click_js(self, timeout=10):
        element = self.wait_until_is_visible(timeout)
        DriverFactory.get_instance().execute_script('arguments[0].click();', element.wrapped_element)

    def get_attribute(self, element_attribute, sanitize=True, timeout=20):
        element = self.wait_until_is_visible(timeout)
        return element.get_attribute(element_attribute).lower().strip() if sanitize else element.get_attribute(
            element_attribute)

    def clear_text(self, timeout=20):
        element = self.wait_until_is_visible(timeout)
        element.clear()

    def is_checked(self, timeout=20):
        element = self.wait_until_is_visible(timeout)
        return element.isSelected()

    def exist_child_element(self, by):
        by_constructed = {'strategy': by[0], 'value': by[1]}
        return self.element().find_elements(by_constructed['strategy'], by_constructed['value']) != []

    def get_child_element(self, by):
        by_constructed = {'strategy': by[0], 'value': by[1]}
        element = self.element().find_element(by_constructed['strategy'], by_constructed['value'])
        return ElementFromFound(found_element=element, parent=self.parent, context=self._context)


class ElementFromLocator(Element):
    def __init__(self, by, parent, context):
        """
        Constructor: Get element based on locator
        :param by: current selenium locator strategy
        :param parent: web object or web page parent of the web object
        :param context: root_element -> element of section for faster search proposes if is null is _driver
        """
        super().__init__(parent, context)
        self.by = by
        self.find_by = FinderService(context)
        self.by_constructed = {'strategy': self.by[0], 'value': self.by[1]}

    def element(self):
        return self.find_by.get_element(self.by, self._context)

    def click(self, timeout=10):
        wait = WebDriverWait(self._context, timeout)
        element = wait.until(ec.element_to_be_clickable(self.by))
        if element is not None:
            element.click()

    def click_only_visible(self, timeout=20):
        element = self.wait_until_is_visible(timeout)
        if element is not None:
            element.click()

    def click_js_only_visible(self, timeout=20):
        element = self.wait_until_is_visible(timeout)
        if element is not None:
            self.click_js()

    def wait_until_exist(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.presence_of_element_located(self.by))

    def wait_until_not_exist(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until_not(ec.presence_of_element_located(self.by))

    def wait_until_is_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.visibility_of_element_located(self.by))

    def wait_until_transition(self, timeout_disappears=20, timeout_visible=4):
        self.wait_until_is_visible(timeout_visible)
        self.wait_until_is_not_visible(timeout_disappears)

    def wait_until_is_not_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until_not(ec.visibility_of_element_located(self.by))

    def element_exist(self):
        return self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value']) != []


class ElementFromFound(Element):
    def __init__(self, found_element, parent, context):
        """
        Constructor: create element from element
        :param found_element: Base element to reduce search scope
        :param parent: web object or web page parent of the web object
        :param context: root_element -> element of section for faster search proposes if is null is _driver
        """
        super().__init__(parent, context)
        self.found_element = found_element
        self.find_by = FinderService(context)

    def element(self):
        return self.found_element

    def click(self, *args):
        element = self.wait_until_is_visible(*args)
        if element is not None:
            element.click()

    def wait_until_is_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.visibility_of(self.found_element))

    def wait_until_transition(self, timeout_disappears=20, timeout_visible=4):
        self.wait_until_is_visible(timeout_visible)
        self.wait_until_is_not_visible(timeout_disappears)

    def wait_until_is_not_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.invisibility_of_element(self.found_element))
