from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateAnAccountPage(BasePage):
    _title = by(how=By.CSS_SELECTOR, using='.radio-inline label', multiple=True)
    _first_name = by(how=By.CSS_SELECTOR, using='#customer_firstname')
    _last_name = by(how=By.CSS_SELECTOR, using='#customer_lastname')
    _email = by(how=By.CSS_SELECTOR, using='#email')
    _password = by(how=By.CSS_SELECTOR, using='#passwd')

    # date of birth
    _day = by(how=By.CSS_SELECTOR, using='#days')
    _month = by(how=By.CSS_SELECTOR, using='#months')
    _year = by(how=By.CSS_SELECTOR, using='#years')

    # address
    _first_name_address = by(how=By.CSS_SELECTOR, using='#firstname')
    _last_name_address = by(how=By.CSS_SELECTOR, using='#lastname')
    _company = by(how=By.CSS_SELECTOR, using='#company')
    _address = by(how=By.CSS_SELECTOR, using='#address1')
    _city = by(how=By.CSS_SELECTOR, using='#city')
    _state = by(how=By.CSS_SELECTOR, using='#id_state')
    _zip_code = by(how=By.CSS_SELECTOR, using='#postcode')
    _country = by(how=By.CSS_SELECTOR, using='#id_country')
    _additional_information = by(how=By.CSS_SELECTOR, using='#other')
    _home_phone = by(how=By.CSS_SELECTOR, using='#phone')
    _mobile_phone = by(how=By.CSS_SELECTOR, using='#phone_mobile')
    _alias = by(how=By.CSS_SELECTOR, using='#alias')

    _register_button = by(how=By.CSS_SELECTOR, using='#submitAccount')

    def create_account_for_ecommerce(self, registration_model):
        self._title().wait_until_all_elements_visible(timeout=60)
        self._title().click_with_text(registration_model['title'])
        self._first_name().send_keys(registration_model['first_name'])
        self._last_name().send_keys(registration_model['last_name'])
        self._password().send_keys(registration_model['password'])

        day_select = Select(self._day().element())
        day_select.select_by_value('15')

        month_select = Select(self._month().element())
        month_select.select_by_index(1)

        year_select = Select(self._year().element())
        year_select.select_by_value('2020')

        self._first_name_address().send_keys(registration_model['first_name'])
        self._last_name_address().send_keys(registration_model['last_name'])
        self._company().send_keys(registration_model['company'])
        self._address().send_keys(registration_model['address'])
        self._city().send_keys(registration_model['city'])

        state_select = Select(self._state().element())
        state_select.select_by_visible_text(registration_model['state'])

        self._zip_code().send_keys(registration_model['password'])

        select_country = Select(self._country().element())
        select_country.select_by_visible_text(registration_model['country'])

        self._additional_information().send_keys(registration_model['additional_information'])
        self._home_phone().send_keys(registration_model['home_phone'])
        self._mobile_phone().send_keys(registration_model['mobile_phone'])
        self._alias().send_keys(registration_model['alias'])
        self._register_button().click()
