from os.path import expanduser
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(expanduser(r'~\pictures\maxresdefault.jpg'))

hist = cv2.calcHist([image], [0], None, [256], [0,256])
plt.hist(image.ravel(), 256, [0,256])
plt.show()

color = ('b', 'g', 'r')

for i, c in enumerate(color):
    hist2 = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist2, color=c)
plt.show()