import time
import logging
import pygetwindow

logger = logging.getLogger(__name__)


class Launcher:
    instance = None
    title = 'Ankama Launcher'

    def __init__(self):
        self.window = self._window()
        if not self.window:
            raise BaseException('No {window} window have been found. Please launch the {window}'.format(window=self.title))
        self.maximize()

    @classmethod
    def factory(cls):
        if cls.instance is None:
            cls.instance = cls()
        assert isinstance(cls.instance, cls)
        return cls.instance

    def _window(self):
        window = pygetwindow.getWindowsWithTitle(self.title)
        logger.info('Found {count} window for {title}'.format(count=len(window), title=self.title))
        return next(iter(window), None)

    @property
    def is_maximized(self):
        return self.window.isMaximized

    @property
    def size(self):
        size = self.window.size
        logger.info('{window} is size {size}'.format(window=self.title, size=size))
        return size

    @property
    def topleft(self):
        topleft = self.window.topleft
        logger.info('{window} have topleft {topleft}'.format(window=self.title, topleft=topleft))
        return topleft

    @property
    def bottomright(self):
        bottomright = self.window.bottomright
        logger.info('{window} have bottomright {bottomright}'.format(window=self.title, bottomright=bottomright))
        return bottomright

    def maximize(self):
        logger.info('Maximizing {window}'.format(window=self.title))
        self.window.maximize()

    def close(self):
        logger.info('Closing {window}'.format(window=self.title))
        self.window.close()
        time.sleep(5)
