import cv2
from os.path import expanduser
from matplotlib import pyplot as plt

img = cv2.imread(expanduser(r'~\pictures\maxresdefault.jpg'), 0)  #  뒤에 0 주면 자동으로 흑백으로 읽음

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

print(ret)
cv2.imshow('Original', img)
cv2.imshow('binary', thresh1)
cv2.imshow('binary_inv', thresh2)
cv2.imshow('trunc', thresh3)
cv2.imshow('tozero', thresh4)
cv2.imshow('tozero_inv', thresh5)


cv2.waitKey(0)
cv2.destroyAllWindows()



