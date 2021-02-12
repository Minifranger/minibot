import os
import logging
from functools import wraps

from pyautogui import locateCenterOnScreen, locateAllOnScreen

logger = logging.getLogger(__name__)


class Media:
    instance = None
    path = None
    wait = None

    class Decorators:
        @classmethod
        def wait(cls, **kwargs):
            def decorator(f):
                @wraps(f)
                def wrapper(self, *args, **kwargs):
                    kwargs.update(minSearchTime=kwargs.get('wait') or self.wait)
                    return f(self, *args, **kwargs)
                return wrapper
            return decorator

    @classmethod
    def factory(cls):
        if cls.instance is None:
            cls.instance = cls()
        assert isinstance(cls.instance, cls)
        return cls.instance

    @Decorators.wait()
    def locate(self, *args, **kwargs):
        path = os.path.join(self.path, *args)
        locate = locateCenterOnScreen(path, **kwargs)
        if locate:
            logger.info('{path} have been located on the screen'.format(path=path))
        else:
            logger.info('{path} have not been located on the screen'.format(path=path))
        return locate
