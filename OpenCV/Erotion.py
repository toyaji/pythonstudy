from os.path import expanduser
import numpy as np
import cv2

def morph(file):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3), np.int8)

    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def morphology(file):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5,5), np.int8)

    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def makeKernel():
    m1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    m2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    m3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

    print(m1, m2, m3)


if __name__ == '__main__':
    file = expanduser(r'~\pictures\kadisoka-free-font.jpg')
    morph(file)
    morphology(file)
    makeKernel()