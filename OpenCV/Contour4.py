from os.path import expanduser

import cv2
import numpy as np


def contour(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    ret, thr = cv2.threshold(img, 127, 255, 0)
    _, contours, hirearchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = max(contours, key=cv2.contourArea)

    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)


    for i in range(defects.shape[0]):
        sp, ep, fp, dist = defects[i, 0]
        start = tuple(cnt[sp][0])
        end = tuple(cnt[ep][0])
        far = tuple(cnt[fp][0])
        cv2.circle(img, far, 3, (0,255,255), -1)

    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    file = expanduser(r'~\Pictures\paul.jpg')
    contour(file)


