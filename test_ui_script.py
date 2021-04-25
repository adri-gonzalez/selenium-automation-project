# IMPORT LIBRARIES
from uuid import uuid4
from config.settings import Settings
from utils.load_env import load_dotenv
from utils.init_page import initial_page, create_page
from SAF.web_driver.driver_factory import DriverFactory

# IMPORT PROJECT PAGES
from pages.landing_page import LandingPage
from pages.authentication_page import AuthenticationPage
from pages.create_an_account_page import CreateAnAccountPage
from pages.my_account_page import MyAccountPage

load_dotenv()

# create webdriver
DriverFactory().get_instance()
landing_page = initial_page(Settings.get_base_url(), LandingPage)
landing_page.click_on_sign_in()

email_guid = str(uuid4())[:4]
authentication_page = create_page(AuthenticationPage)
authentication_page.create_account(f'incluit.test+{email_guid}@gmail.com')

registration_model = {
    'title': 'Mr.',
    'first_name': 'Test',
    'last_name': 'Practice',
    'email': 'test_practice@incluit.com',
    'password': '33021',

    'company': 'Incluit',
    'address': '(305) 234-3559 9715 SW 161st St Miami, Florida(FL), 33157',
    'second_address': '',
    'city': 'Miami',
    'state': 'Florida',
    'zip_code': '33021',
    'country': 'United States',
    'additional_information': 'Additional Information',
    'home_phone': '+15055555555',
    'mobile_phone': '+15055555554',
    'alias': 'alias test',
}
create_account_page = create_page(CreateAnAccountPage)
create_account_page.create_account_for_ecommerce(registration_model)

my_account_page = create_page(MyAccountPage)
my_account_page.all_elements_are_visible()

print(my_account_page.get_order_history_and_details_text())
print(my_account_page.get_my_credit_slips_text())
print(my_account_page.get_my_address_text())
print(my_account_page.get_my_personal_information_text())
print(my_account_page.get_my_wish_lists_text())
print(my_account_page.get_info_account_text())

DriverFactory.dispose_instance()
