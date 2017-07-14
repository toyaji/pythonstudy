from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from win32gui import GetActiveWindow, GetDC, GetPixel, GetWindowText, GetForegroundWindow
from win32api import SetCursorPos, mouse_event
import time
from random import randint




def click(x,y):
    SetCursorPos((x,y))
    mouse_event(MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    mouse_event(MOUSEEVENTF_LEFTUP,x,y,0,0)

def posegener():
    # x, y = randint(539, 771), randint(201, 415)
    x, y = randint(536, 771), randint(179, 532)
    time = randint(1, 3) / 1000
    return (x, y, time)

def test_small():
    win = GetDC(GetActiveWindow())
    # 작은창일때 체킹포인트
    color1 = GetPixel(win, 543, 419)
    color2 = GetPixel(win, 741, 433)
    color3 = GetPixel(win, 704, 188)

    # 큰창일때 체킹포인트
    click(684, 362)
    color4 = GetPixel(win, 544, 597)
    color5 = GetPixel(win, 546, 581)

    colorbool1 = str(color1)[0] == '6'
    colorbool2 = str(color2)[0] in ['8', '6']
    colorbool3 = str(color3)[:2] == '16'

    colorbool4 = str(color4)[0] == '6'
    colorbool5 = str(color5)[:2] == '16'


    if colorbool1 & colorbool2 & colorbool3:
        return "small"
    elif colorbool4 & colorbool5:
        return "big"
    else:
        print("False")
        return False

def windows_test():
    name = GetWindowText(GetForegroundWindow())
    if name[:7] != 'samsung':
        return False

def avoid_Box(x, y):
    # box area : 649 - 673  255-283
    bol = bool
    if x > 649 & x < 673 & y > 255 & y < 283:
    # if x > 647 & x < 673 & y > 356 & y < 380:
        bol = True
    else:
        bol = False
    return bol

def take_picture():
    if test_small() == 'small':
        click(753, 600)
        time.sleep(3.5)

    click(687, 595)
    time.sleep(1.5)
    click(652, 583)
    time.sleep(1.5)
    click(653, 565)
    time.sleep(1.5)
    click(759, 590)
    time.sleep(1.5)
    click(759, 590)
    time.sleep(1.5)

def skill_begin():
    if test_small() == 'big':
        click(753, 600)
        time.sleep(2.4)

    click(551, 601)
    time.sleep(0.3)
    click(673, 483)
    time.sleep(0.2)
    click(624, 483)
    time.sleep(0.2)
    click(566, 483)
    time.sleep(2.2)


if __name__ == '__main__':

    # (940, 250) ~ (1250, 750)
    time.sleep(3)
    skill_begin()
    for i in range(100):
        for _ in range(300):
            if windows_test() == False:
                print("Check your Window")
                exit()

            x, y, t = posegener()
            flag = test_small()

            if flag == 'big':
                click(x, y)
            elif flag == 'small':
                click(753, 600)

        take_picture()

