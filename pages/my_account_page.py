from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    _order_history_and_details = by(how=By.CSS_SELECTOR, using='a[title="Orders"] span')
    _my_credit_slips = by(how=By.CSS_SELECTOR, using='a[title="Credit slips"] span')
    _my_address = by(how=By.CSS_SELECTOR, using='a[title="Addresses"] span')
    _my_personal_information = by(how=By.CSS_SELECTOR, using='a[title="Information"] span')
    _my_wish_lists = by(how=By.CSS_SELECTOR, using='a[title="My wishlists"] span')
    _info_account = by(how=By.CSS_SELECTOR, using='.info-account')

    def all_elements_are_visible(self):
        self._order_history_and_details().wait_until_is_visible()
        self._my_credit_slips().wait_until_is_visible()
        self._my_address().wait_until_is_visible()
        self._my_personal_information().wait_until_is_visible()
        self._my_wish_lists().wait_until_is_visible()
        return True

    def get_order_history_and_details_text(self):
        return self._order_history_and_details().get_text()

    def get_my_credit_slips_text(self):
        return self._my_credit_slips().get_text()

    def get_my_address_text(self):
        return self._my_address().get_text()

    def get_my_personal_information_text(self):
        return self._my_personal_information().get_text()

    def get_my_wish_lists_text(self):
        return self._my_wish_lists().get_text()

    def get_info_account_text(self):
        return self._info_account().get_text()
