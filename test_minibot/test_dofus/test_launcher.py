import unittest
from pyscreeze import Point

from minibot.ankama.launcher.launcher import Launcher


class TestLauncher(unittest.TestCase):

    def setUp(self):
        self.launcher = Launcher.factory()

    def test_window(self):
        window = Launcher.instance.window
        assert window
        assert window.title == Launcher.instance.title

    def test_size(self):
        w, h = Launcher.instance.size
        assert w > 0, h > 0
        assert isinstance(w, int)
        assert isinstance(h, int)

    def test_topleft(self):
        x, y = Launcher.instance.topleft
        assert isinstance(x, int)
        assert isinstance(y, int)

    def test_bottomright(self):
        x, y = Launcher.instance.bottomright
        assert isinstance(x, int)
        assert isinstance(y, int)

    def test_is_maximized(self):
        Launcher.instance.maximize()
        assert Launcher.instance.is_maximized

    def test_is_activated(self):
        Launcher.instance.activate()
        assert Launcher.instance.is_activated

    def test_dofus(self):
        dofus = Launcher.instance.dofus()
        assert isinstance(dofus, Point)

    def test_open(self):
        Launcher.instance.open()
        assert Launcher.instance._window()

    def test_close(self):
        Launcher.instance.close()
        assert Launcher.instance._window() is None
