from os.path import expanduser
import cv2
import numpy as np

filename1 = expanduser(r'~\Pictures\maldives1.jpg')
filename2 = expanduser(r'~\Pictures\maxresdefault.jpg')

def onMouse(x):
    pass

def blending(filename1, filename2):
    img1 = cv2.imread(filename1)
    img2 = cv2.imread(filename2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('Mixing', 'ImgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('Mixing', 'ImgPane')

    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
        cv2.imshow('ImgPane', img)

        k = cv2.waitKey(1) % 0xFF
        if k == 27: break

        mix = cv2.getTrackbarPos('Mixing', 'ImgPane')

    cv2.destroyAllWindows()


def bitoperation(hpos, vpos):
    global filename1

    img1 = cv2.imread(filename1)
    img2 = cv2.imread(expanduser(r'~\Pictures\paul.jpg'))

    # 사진 중첩시키기
    rows, cols, channels = img2.shape
    roi = img1[vpos:vpos+rows, hpos:hpos+cols]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY)
    #
    mask_inv = cv2.bitwise_not(mask)
    # 마스크값이 0이 아닌 부분만 인자, x 와 y 를 and 연산시킴
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:vpos+rows, hpos:hpos+cols] = dst

    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    bitoperation(10, 10)

if __name__ == '__main__':
    blending(filename1, filename2)