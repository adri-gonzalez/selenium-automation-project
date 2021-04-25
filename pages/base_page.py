from pages.header_page import HeaderPage
from pages.footer_page import FooterPage
from SAF.pages.abstract_page_object import AbstractPageObject
from SAF.pages.page_factory import callable_find_by_wo as by_wo
from selenium.webdriver.common.by import By


class BasePage(AbstractPageObject):
    header_wo = by_wo(HeaderPage, how=By.CSS_SELECTOR, using='')
    footer_wo = by_wo(FooterPage, how=By.CSS_SELECTOR, using='')

    def wait_until_page_finish_load(self, timeout=60):
        self.navigation_service.wait_until_document_ready(timeout)
