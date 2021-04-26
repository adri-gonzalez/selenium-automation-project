from SAF.pages.abstract_web_object import AbstractWebObject
from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By


class FooterPage(AbstractWebObject):
    # newsletter
    _enter_your_email = by(how=By.CSS_SELECTOR, using='#newsletter-input')
    _submit_email = by(how=By.CSS_SELECTOR, using='button[name="submitNewsletter"]')

    # social block
    _facebook = by(how=By.CSS_SELECTOR, using='#social_block li[class="facebook"]')
    _twitter = by(how=By.CSS_SELECTOR, using='#social_block li[class="twitter"]')
    _youtube = by(how=By.CSS_SELECTOR, using='#social_block li[class="youtube"]')
    _google_plus = by(how=By.CSS_SELECTOR, using='#social_block li[class="google-plus"]')

    # categories
    _women = by(how=By.CSS_SELECTOR, using='')

    # information
    _specials = by(how=By.CSS_SELECTOR, using='a[title="Specials"]')
    _new_products = by(how=By.CSS_SELECTOR, using='a[title="New products"]')
    _best_sellers = by(how=By.CSS_SELECTOR, using='a[title="Best sellers"]')
    _our_stores = by(how=By.CSS_SELECTOR, using='a[title="Our stores"]')
    _contact_us = by(how=By.CSS_SELECTOR, using='a[title="Contact us"]')
    _terms_and_conditions = by(how=By.CSS_SELECTOR, using='a[title="Terms and conditions of use"]')
    _about_us = by(how=By.CSS_SELECTOR, using='a[title="About us"]')
    _site_map = by(how=By.CSS_SELECTOR, using='a[title="Sitemap"]')

    # my account
    _my_orders = by(how=By.CSS_SELECTOR, using='a[title="My orders"]')
    _my_credit_slips = by(how=By.CSS_SELECTOR, using='a[title="My credit slips"]')
    _my_addresses = by(how=By.CSS_SELECTOR, using='a[title="My addresses"]')
    _my_personal_info = by(how=By.CSS_SELECTOR, using='a[title="Manage my personal information"]')

    # store information
    _location = by(how=By.CSS_SELECTOR, using='#block_contact_infos li:nth-child(1)')
    _phone_number = by(how=By.CSS_SELECTOR, using='#block_contact_infos li:nth-child(2)')
    _email = by(how=By.CSS_SELECTOR, using='#block_contact_infos li:nth-child(3)')
