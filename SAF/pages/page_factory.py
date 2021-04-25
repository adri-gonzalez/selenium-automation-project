from pydash import map_
from SAF.pages.element import ElementFromLocator
from SAF.pages.elements import ElementCollection

__all__ = ['cacheable', 'callable_find_by', 'property_find_by', 'callable_find_by_wo']


def cacheable_decorator(lookup):
    def func(self):
        if not hasattr(self, '_elements_cache'):
            self._elements_cache = {}
        cache = self._elements_cache

        key = id(lookup)
        if key not in cache:
            cache[key] = lookup(self)
        return cache[key]

    return func


cacheable = cacheable_decorator

_strategy_kwargs = ['id_', 'xpath', 'link_text', 'partial_link_text',
                    'name', 'tag_name', 'class_name', 'css_selector']


def _callable_find_by(how, using, multiple, cacheable, context, **kwargs):
    def element_finder(self):
        # context - driver or a certain element
        if context:
            ctx = context() if callable(context) else context.__get__(self)  # or property
        else:
            ctx = getattr(self, "get_root_element")() if hasattr(self, 'get_root_element') else getattr(self, "_driver")

        if how and using:
            return ElementFromLocator(by=(how, using), parent=self, context=ctx)

    def elements_finder(self):
        if context:
            ctx = context() if callable(context) else context.__get__(self)  # or property
        else:
            ctx = getattr(self, "get_root_element")() if hasattr(self, 'get_root_element') else getattr(self, "_driver")

        if how and using:
            return ElementCollection(by=(how, using), parent=self, context=ctx)

    return elements_finder if multiple else element_finder


def _callable_find_by_wo(web_object_class, how, using, multiple, context):
    def web_object_finder(self):
        # context - driver or a certain element
        if context:
            ctx = context() if callable(context) else context.__get__(self)  # or property
        else:
            ctx = getattr(self, "get_root_element")() if hasattr(self, 'get_root_element') else getattr(self, "_driver")

        # 'how' AND 'using' take precedence over keyword arguments
        if how and using:
            return map_(ctx.find_elements(how, using),
                        lambda x: web_object_class(self, (how, using), ctx, x)) if multiple else web_object_class(
                self,
                (how,
                 using), ctx)

    return web_object_finder


def callable_find_by(how=None, using=None, multiple=False, cacheable=False, context=None,
                     **kwargs):
    return _callable_find_by(how, using, multiple, cacheable, context, **kwargs)


def callable_find_by_wo(web_object_class=None, how=None, using=None, multiple=False, context=None):
    return _callable_find_by_wo(web_object_class, how, using, multiple, context)


def property_find_by(how=None, using=None, multiple=False, cacheable=False, context=None,
                     **kwargs):
    return property(_callable_find_by(how, using, multiple, cacheable, context, **kwargs))
