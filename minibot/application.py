import subprocess
import time
import logging
from functools import wraps

from pyautogui import getWindowsWithTitle
from pyscreeze import Point

logger = logging.getLogger(__name__)


class Application:
    instance = None
    path = None
    title = None
    subprocess = None

    class Decorators:
        @classmethod
        def activated(cls, f):
            @wraps(f)
            def wrapper(self, *args, **kwargs):
                self.activate()
                return f(self, *args, **kwargs)

            return wrapper

        @classmethod
        def validate(cls, f):
            @wraps(f)
            def wrapper(self, *args, **kwargs):
                point = f(self, *args, **kwargs)
                inside = self.inside(point=point)
                if inside is False:
                    logger.info('Point is not inside the window {window}'.format(window=self.title))
                return point if inside else None

            return wrapper

    def __init__(self, **kwargs):
        self.open()
        self.window = self._window()
        self.maximize()

    @classmethod
    def factory(cls, **kwargs):
        if cls.instance is None:
            cls.instance = cls(**kwargs)
        assert isinstance(cls.instance, cls)
        return cls.instance

    def _window(self):
        window = getWindowsWithTitle(self.title)
        logger.debug('Found {count} window for {title}'.format(count=len(window), title=self.title))
        return next(iter(window), None)

    @property
    def is_maximized(self):
        return self.window.isMaximized

    @property
    def is_activated(self):
        return self.window.isActive

    @property
    def size(self):
        size = self.window.size
        logger.debug('{window} is size {size}'.format(window=self.title, size=size))
        return size

    @property
    def topleft(self):
        topleft = self.window.topleft
        logger.debug('{window} have topleft {topleft}'.format(window=self.title, topleft=topleft))
        return topleft

    @property
    def bottomright(self):
        bottomright = self.window.bottomright
        logger.debug('{window} have bottomright {bottomright}'.format(window=self.title, bottomright=bottomright))
        return bottomright

    def inside(self, **kwargs):
        point = kwargs.get('point')
        return self.topleft < point < self.bottomright if isinstance(point, Point) else None

    def maximize(self):
        logger.info('Maximizing {window}'.format(window=self.title))
        self.window.maximize()

    # TODO : add decorator for open, close and activate
    def open(self):
        if not self._window():
            logger.info('Opening {window}'.format(window=self.title))
            self.subprocess = subprocess.Popen(self.path)
            while not self._window():
                time.sleep(1)
        else:
            logger.info('{window} is already opened'.format(window=self.title))

    def close(self):
        if self._window():
            logger.info('Closing {window}'.format(window=self.title))
            self.window.close()
            while self._window():
                time.sleep(1)
        else:
            logger.info('{window} is already closed'.format(window=self.title))

    def activate(self):
        if not self.is_activated:
            logger.info('Activating {window}'.format(window=self.title))
            self.window.activate()
            while not self.is_activated:
                time.sleep(1)
        else:
            logger.info('{window} is already activated'.format(window=self.title))


class Element:
    instance = None

    @classmethod
    def factory(cls):
        if cls.instance is None:
            cls.instance = cls()
        assert isinstance(cls.instance, cls)
        return cls.instance
