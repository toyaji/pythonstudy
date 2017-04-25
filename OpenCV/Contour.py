from os.path import expanduser
import cv2

def contour(image):
    img = cv2.imread(image)
    img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    cv2.drawContours(img, contours, -1, (0, 255, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = expanduser(r'~\pictures\strawberry.jpg')
    contour(image)