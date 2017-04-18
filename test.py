import win32gui
import time


if __name__ == '__main__':

    while True:
        win = win32gui.GetActiveWindow()
        print(win)
        x, y = win32gui.GetCursorPos()
        print(x, y)
        color = win32gui.GetPixel(win32gui.GetDC(win), x, y)
        print(color)
        name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        print(name)
        time.sleep(2)