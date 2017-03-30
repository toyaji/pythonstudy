import numpy as np
import cv2
from os.path import expanduser

if __name__ == '__main__':
    img1 = cv2.imread(expanduser(r'~\Pictures\maldives1.jpg'))
    img2 = cv2.imread(expanduser(r'~\Pictures\maxresdefault.jpg'))

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    img3 = img1 + img2
    img4 = cv2.add(img1, img2)

    cv2.imshow('img3', img3)
    cv2.imshow('img4', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()