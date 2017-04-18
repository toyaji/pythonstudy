import win32api, win32con, win32gui
import time
from random import randint




def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def posegener():
    x, y = randint(536, 771), randint(179, 532)
    time = randint(1, 3) / 1000
    return (x, y, time)

def get_pixel():
    win = win32gui.GetActiveWindow()
    test = win32gui.GetPixel(win32gui.GetDC(win), 542, 403)
    if test > 12000000:
        click(756, 602)
        time.sleep(1)
    color1 = win32gui.GetPixel(win32gui.GetDC(win), 541, 580)
    color2 = win32gui.GetPixel(win32gui.GetDC(win), 543, 597)
    if color1 > 15000000 or color2 < 8000000:
        return True
    else:
        return True

def windows_test():
    name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if name[:7] != 'samsung':
        return False

def tBox():
    pass
#color < 118 ..... / (661, 522)


if __name__ == '__main__':

# (940, 250) ~ (1250, 750)
    time.sleep(5)
    start = time.time()
    for _ in range(10000) :
        if windows_test() == False:
            print("Check your Window")
            exit()

        x, y, t = posegener()
        bol = get_pixel()

        if bol:
            click(x, y)
        else:
            time.sleep(10)
            click(768, 180)
            time.sleep(0.5)
            click(684, 530)
            continue

        time.sleep(t)

    print(time.time() - start)





