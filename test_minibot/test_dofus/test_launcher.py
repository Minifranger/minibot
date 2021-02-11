import unittest

from minibot.dofus.launcher import Launcher


class TestLauncher(unittest.TestCase):
    launcher = Launcher.factory()

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

    def test_close(self):
        Launcher.instance.close()
        assert Launcher.instance._window() is None
