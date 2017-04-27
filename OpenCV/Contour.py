from os.path import expanduser
import cv2

def contour(image):
    img = cv2.imread(image)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    cv2.drawContours(img, contours, -1, (0, 255, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def moment(image):
    """폐곡선이 Contour 의 면적, 중신, 둘게 같읕 특성 구하는데 이용됨"""
    img = cv2.imread(image)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour = contours[40]
    mmt = cv2.moments(contour)

    for key, val in mmt.items():
        print('%s:\t%.5f' % (key, val))

    # 무게 중심 구하는 식임 - m00 이 면적임
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    print(cx, cy)

def contourArea(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    ret, thr = cv2.threshold(img, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]
    area = cv2.contourArea(cnt)
    perimeter= cv2.arcLength(cnt, True)   # 뒤에 트루면 폐곡선, 아니면 호인 Contour임

    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    print('contour 면적 :', area)
    print('contour 길이: ', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def approximation(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    ret, thr = cv2.threshold(img, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[40]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    epsilon1 = 0.01 * cv2.arcLength(cnt, True)
    epsilon2 = 0.1 * cv2.arcLength(cnt, True)

    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(img, [approx1], 0, (0, 255, 0), 3)
    cv2.drawContours(img, [approx2], 0, (0, 0, 255), 2)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def

if __name__ == '__main__':
    image = expanduser(r'~\pictures\paul.jpg')
    # image = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    contour(image)
    moment(image)
    contourArea(image)
    approximation(image)
