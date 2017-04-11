import cv2
import numpy as np
from os.path import expanduser
from matplotlib import pyplot as plt



def thresholding(img):
    ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 70)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 71, 70)

    titles = ['original', 'Global Thresholding (v=127)', 'Adaptive MEAN', 'Adaptive GAUSSIAN']
    images = [img, th1, th2, th3]

    for i in range(4):
        cv2.imshow(titles[i], images[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def otsu_thresholding(img):
    ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blur = cv2.GaussianBlur(img, (5,5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
              'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
              'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

    for i in range(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread(expanduser(r'~\pictures\windsong.jpg'))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresholding(img)

    img = cv2.imread(expanduser(r'~\pictures\paul.jpg'))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    otsu_thresholding(img)