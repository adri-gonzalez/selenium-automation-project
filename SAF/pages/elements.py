from pydash import find, map_
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SAF.pages.element import ElementFromFound


class ElementCollection:
    """
    Base Element class to return from page factory
    Should not be instantiated directly
    """

    def __init__(self, by, parent, context):
        """
        Constructor
        :param by: current selenium locator strategy
        :param parent: web object or web page parent of the web object
        :param context: root_element -> element of section for faster search proposes if is null is _driver
        """
        self.parent = parent
        self._context = context
        self.by = by
        self.by_constructed = {'strategy': self.by[0], 'value': self.by[1]}

    def elements(self):
        return map_(self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value']),
                    lambda x: ElementFromFound(found_element=x, parent=self.parent, context=self._context))

    def click_with_text(self, text, exist_only=False, *args):
        if exist_only:
            elements = self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value'])
        else:
            elements = self.wait_until_exist_all_elements(*args)
        element = find(elements, lambda x: self._sanitize_text(x.text) == self._sanitize_text(text))
        if element is not None:
            element.click()
        else:
            raise Exception('not exist element')

    def send_keys(self, value, existence=False, *args):
        element = self.wait_until_exist_all_elements(*args) if existence else self.wait_until_all_elements_visible(
            *args)
        if element is not None:
            element.send_keys(value)

    def wait_until_exist_all_elements(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.presence_of_all_elements_located(self.by))

    def wait_until_all_elements_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(ec.visibility_of_all_elements_located(self.by))

    def wait_until_all_element_not_visible(self, timeout=20):
        wait = WebDriverWait(self._context, timeout)
        return wait.until(not ec.presence_of_all_elements_located(self.by))

    def get_all_text_elements(self, text_sanitize=True, exist_only=False):
        if exist_only:
            elements = self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value'])
        else:
            elements = self.wait_until_all_elements_visible()
        return map_(elements, lambda x: x.text.lower().strip() if text_sanitize else x.text)

    def elements_exist(self):
        return self._context.find_elements(self.by_constructed['strategy'], self.by_constructed['value']) != []

    def click_with_index(self, index, *args):
        elements = self.wait_until_all_elements_visible(*args)
        elements[index].click()

    def _sanitize_text(self, text):
        return text.lower().strip()
