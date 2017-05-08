from os.path import expanduser

import cv2
import numpy as np

def convex(image, th):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    ret, thr = cv2.threshold(img, 240, 255, 0)

    cv2.imshow('thresh', thr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    _, contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    cnt = max(contour_sizes, key=lambda x: x[0])[1]
    #cnt = contours[th]


    mmt = cv2.moments(cnt)
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    # 컨투어에 외접하는 원 구함
    x, y, w, h = cv2.boundingRect(cnt)
    korea_rect_area = w*h
    korea_area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    ellipse = cv2.fitEllipse(cnt)

    aspect_ration = w/h
    extent = korea_area/korea_rect_area
    solidity = korea_area/hull_area

    print(aspect_ration, extent, solidity, ellipse)

    equivalent_diameter = 2*np.sqrt(korea_area/np.pi)
    korea_radius = int(equivalent_diameter/2)

    cv2.circle(img, (cx, cy), 3, (0,0,255), -1)
    cv2.circle(img, (cx, cy), korea_radius, (0,0,255), 2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
    cv2.ellipse(img, ellipse, (50,50,50), 2)

    cv2.imshow('Korea Features', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = expanduser(r'~\pictures\str.jpg')
    convex(image, 0)