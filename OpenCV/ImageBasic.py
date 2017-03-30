import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread(r'C:\Users\user\Pictures\externalFile.jpg')
    B, G, R = img[340, 200]
    print(B, G, R)

    cv2.imshow('origin', img)

    # 이미지의 특정 영역 자르는 방법
    cut = img[300:400, 350:600]
    cv2.imshow('cutted', cut)

    print(img.shape)
    print(cut.shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # RGB 별로 쪼개서 2차원 행렬로 나눠줌
    b, g, r = cv2.split(img)
    print(img[100, 100])
    print(b[100, 100], g[100, 100], r[100, 100])

    cv2.imshow('bluechannel', b)
    cv2.imshow('greenchannel', g)
    cv2.imshow('redchannel', r)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # RGB 별로 있는거를 합치는 방법
    merge = cv2.merge((b, g, r))
    cv2.imshow('merged', merge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()