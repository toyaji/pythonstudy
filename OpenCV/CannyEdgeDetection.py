from os.path import expanduser
import cv2


def canny(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 1000, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = expanduser(r'~\pictures\strawberry.jpg')
    canny(image)