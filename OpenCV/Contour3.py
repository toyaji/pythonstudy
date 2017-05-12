import cv2
from os.path import expanduser

def convex_defects(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    ret, thr = cv2.threshold(img, 127, 255, 0)
    img, contours, hir = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('origina', thr)
    cv2.imshow('image', img[3])
    cv2.waitKey(0)

    for cnt in contours:
        print(cnt.shape)

    print(hir.shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    file = expanduser(r'~\Pictures\20170306_200439.jpg')
    convex_defects(file)