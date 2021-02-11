# import win32gui
import pyautogui
import pygetwindow as gw

# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     print("Window %s:" % win32gui.GetWindowText(hwnd))
#     print("\tLocation: (%d, %d)" % (x, y))
#     print("\t    Size: (%d, %d)" % (w, h))
#
# def main():
#     win32gui.EnumWindows(callback, None)
from minibot.dofus.launcher import Launcher

if __name__ == '__main__':
    Launcher.factory()
    print(Launcher.instance.window)
    print(Launcher.instance.is_maximized)
    print(Launcher.instance.size)
    # print(gw.getAllTitles())
    # # print(pyautogui.size())
    # pos = pyautogui.position()
    # while True:
    #     if pyautogui.position() != pos:
    #         pos = pyautogui.position()
    #         print(pos)
    # distance = 200
    # while distance > 0:
    #     pyautogui.drag(distance, 0, duration=0.5)  # move right
    #     distance -= 5
    #     pyautogui.drag(0, distance, duration=0.5)  # move down
    #     pyautogui.drag(-distance, 0, duration=0.5)  # move left
    #     distance -= 5
    #     pyautogui.drag(0, -distance, duration=0.5)  # move up
    # main()

