from SAF.pages.abstract_web_object import AbstractWebObject
from SAF.pages.page_factory import callable_find_by as by
from selenium.webdriver.common.by import By


class HeaderPage(AbstractWebObject):
    """
        HEADER WEB-OBJECT: WEBOBJECT SIGNIFICA QUE ES PARTE DE UNA PAGINA.
        LA IDEA DE IMPLEMENTAR WEB-OBJECTS ES PODER SEGMENTAR UNA GRAN CANTIDAD DE LOGICA
        EN UN ARCHIVO SEPARADO AL PAGE OBJECT MODEL QUE CONTENDRIA ESTA LOGICA
        """
    # banner
    _promotion = by(how=By.CLASS_NAME, using="banner")

    # navigation
    _call_us_now = by(how=By.CSS_SELECTOR, using="span[class='shop-phone']")
    _contact_us = by(how=By.CSS_SELECTOR, using='#contact-link')
    _sign_in = by(how=By.CSS_SELECTOR, using='.login')

    # nav container
    _header_logo = by(how=By.CSS_SELECTOR, using='.logo.img-responsive')
    _search_input = by(how=By.CSS_SELECTOR, using='#search_query_top')
    _search_button = by(how=By.CSS_SELECTOR, using='button[name="submit_search"]')
    _cart = by(how=By.CSS_SELECTOR, using='.shopping_cart > a')

    # top menu
    _women = by(how=By.CSS_SELECTOR, using='#block_top_menu a[title="Women"]')
    _dresses = by(how=By.CSS_SELECTOR, using='#block_top_menu a[title="Dresses"]')
    _t_shirts = by(how=By.CSS_SELECTOR, using='#block_top_menu a[title="T-shirts"]')
