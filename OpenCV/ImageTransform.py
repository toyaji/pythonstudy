import cv2
import numpy as np
from matplotlib import pyplot as plt

def scaling(image):
    img = cv2.imread(image)
    height, width = img.shape[:2]

    img2 = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('original', img)
    cv2.imshow('fx=0.5', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def translation(image):
    img = cv2.imread(image)
    # 칼라 이미지인 경우, 앞에 2개 인자로 제한해야함, 맨 뒤에는 rgb 니까..
    rows, cols = img.shape[:2]

    # 트랜슬레이션 매트릭스 생성해서 이미지 옮기는 방법임 - 3번째 들어가는 값이 이동할 픽셀수
    M = np.float32([[1,0,100], [0,1,50]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotation(image):
    img = cv2.imread(image)
    rows, cols = img.shape[:2]

    M1 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)   # 마지막 1 은 배율임. 축소나 확대가능함
    M2 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

    dst = cv2.warpAffine(img, M1, (cols, rows))
    dst1 = cv2.warpAffine(img, M2, (cols, rows))

    cv2.imshow('45-rotation', dst)
    cv2.imshow('90-rotation', dst1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def simple_ratation(image):
    img = cv2.imread(image)
    rotated_image = cv2.transpose(img)

    cv2.imshow('Rotated Image 2', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def flipped(image):
    img = cv2.imread(image)
    # flipcode 인자가 0 이면 x 축, 양수면 y축, 음수면 양축 다
    flip = cv2.flip(img, 1)
    cv2.imshow('Flipped Image', flip)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def affin_translation(image):
    img = cv2.imread(image)
    rows, cols, ch = img.shape

    # 위에 좌표를 아래 좌표로 바꾸는 변환 하게됨됨
    pst1 = np.float32([[50,50],[200,50],[50,200]])
    pst2 = np.float32([[10,100],[200,50],[100,250]])

    M = cv2.getAffineTransform(pst1, pst2); print(M)
    dst = cv2.warpAffine(img, M, (cols, rows))

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()

def perspective_trans(image):
    img = cv2.imread(image)
    rows, cols, ch = img.shape

    pst1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pst2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    # 원근감 느끼도록 warp 시키는 함수임... 매트릭스 이해하려면 좀 더 공부 필요함
    M = cv2.getPerspectiveTransform(pst1, pst2); print(M)
    dst = cv2.warpPerspective(img, M, (cols, rows))

    plt.subplot(121); plt.imshow(img); plt.title('Input')
    plt.subplot(122); plt.imshow(dst); plt.title('Output')
    plt.show()

def image_pyramid(image):
    img= cv2.imread(image)
    # 50% 200% 로 이미지 사이즈 제조정해줌
    smaller = cv2.pyrDown(img)
    larger = cv2.pyrUp(img)

    cv2.imshow('Smaller', smaller)
    cv2.imshow('Larger', larger)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    from os.path import expanduser

    image = expanduser(r'~\Pictures\paul.jpg')
    image2 = expanduser(r'~\Pictures\CHESS.png')
    translation(image)
    rotation(image)
    flipped(image)
    simple_ratation(image)
    affin_translation(image2)
    perspective_trans(image2)
    image_pyramid(image)