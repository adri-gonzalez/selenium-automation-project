from SAF.utils.constants.func_names import ELEMENT_FUNC, WEB_OBJECT_FUNC, ELEMENTS_FUNC


class PomMeta(type):
    def __new__(cls, what, bases=None, dict_attributes=None):
        new_dict = dict_attributes.copy()

        for key, val in dict_attributes.items():
            if callable(val) and (val.__name__ == ELEMENT_FUNC or val.__name__ == WEB_OBJECT_FUNC):
                new_dict.update(cls._add_helper_methods(cls, key, val))
            if callable(val) and val.__name__ == ELEMENTS_FUNC:
                new_dict.update(cls._add_helper_methods(cls, key, val, True))
        return type.__new__(cls, what, bases, new_dict)

    @staticmethod
    def _add_helper_methods(cls, element_name, func, multiple=False):
        new_dict = {}

        name = element_name if element_name.startswith('_') else f'_{element_name}'

        def exist(self, *args):
            return func(self).wait_until_exist_all_elements(*args) if multiple else func(self).wait_until_exist(*args)

        new_dict[f'wait_until{name}_exist'] = exist

        def is_visible(self, *args):
            return func(self).wait_until_all_elements_visible(*args) if multiple else func(self).wait_until_is_visible(
                *args)

        new_dict[f'wait_until{name}_visible'] = is_visible

        def is_not_visible(self, *args):
            return func(self).wait_until_all_element_not_visible(*args) if multiple else func(
                self).wait_until_is_not_visible(*args)

        new_dict[f'wait_until{name}_disappears'] = is_not_visible

        def get_element_text(self, *args):
            return func(self).get_all_text_elements(*args) if multiple else func(self).get_text(*args)

        new_dict[f'get{name}_text'] = get_element_text

        if multiple:
            def click_option(self, option, *args):
                func(self).click_with_text(option, *args)

            new_dict[f'click{name}_with_text'] = click_option

        else:
            def click(self, *args):
                func(self).click(*args)

            new_dict[f'click_on{name}'] = click

            def send_text(self, text, *args):
                func(self).send_keys(text, *args)

            new_dict[f'send_text_to{name}'] = send_text

        return new_dict
