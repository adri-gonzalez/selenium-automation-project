from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    """
    PAGINA DE CONTACTO, CONTIENE WEB-ELEMENTS Y
    EL COMPORTAMIENNTO DE MANDAR UN MENSAJE
    """
    _subject_heading = by(how=By.CSS_SELECTOR, using='#id_contact')
    _email_address = by(how=By.CSS_SELECTOR, using='#email')
    _order_reference = by(how=By.CSS_SELECTOR, using='#id_order')
    _attach_file = by(how=By.CSS_SELECTOR, using='#fileUpload')s
    _message = by(how=By.CSS_SELECTOR, using='message')
    _send_button = by(how=By.CSS_SELECTOR, using='#submitMessage')

    def send_contact_message(self, subject_model):
        self._subject_heading().send_keys(subject_model['heading'])
        self._email_address().send_keys(subject_model['email'])
        self._order_reference().send_keys(subject_model['order_reference'])
        self._message().send_keys(subject_model['message'])
        self._send_button().click()
