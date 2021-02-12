import os
import subprocess
import time
import logging
from functools import wraps

import pyautogui
from pyautogui import getWindowsWithTitle
from pyscreeze import Point

from minibot.application import Application, Element
from minibot.media import Media

logger = logging.getLogger(__name__)


class Launcher(Application):
    title = 'Ankama Launcher'

    def __init__(self, **kwargs):
        self.path = kwargs.get('path') or os.getenv('ANKAMA_LAUNCHER')
        super().__init__(**kwargs)
        LauncherMedia.factory()
        Dofus.factory()

    @Application.Decorators.activated
    @Application.Decorators.validate
    def dofus(self):
        dofus = Dofus.instance.logo
        return dofus


class Dofus(Element):

    @property
    def logo(self):
        return LauncherMedia.instance.locate('dofus_logo.png')

    @property
    def play(self):
        return LauncherMedia.instance.locate('dofus_play.png')


class LauncherMedia(Media):
    wait = 10

    path = os.path.join(os.path.dirname(__file__), 'media')
