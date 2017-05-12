import cv2

def convex_defects(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    ret, thr = cv2.threshold(img, 127, 255, 0)