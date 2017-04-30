import cv2
from matplotlib import pyplot as plt
import numpy as np
from os.path import expanduser

green = (0, 255, 0)

def show(image):
    # 사이즈 확인하기
    plt.figure(figsize=(10,10))
    plt.imshow(image, interpolation='nearest')


def overlay_mask(mask, image):
    # rgb 에 마스크 씌우기
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    return img


def find_biggest_contour(image):
    image = image.copy()
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    # 가장 큰 녀석만 따로 떼내기
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    print(contour_sizes)
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

    # 제일 큰 놈만 콘투어 뱉어내기
    mask = np.zeros(image.shape, np.int8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    return biggest_contour, mask


def circle_contour(image, contour):
    # 바운딩하기 ellipse
    image_with_ellipse = image.copy()
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(image_with_ellipse, ellipse, green, 2, cv2.LINE_AA)
    return image_with_ellipse


def find_strawberry(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 정사각형으로 사이즈 제 조정하는건데... 좀 공부해야봐 알듯...?
    max_dimension = max(image.shape)
    scale = 700/max_dimension
    image = cv2.resize(image, None, fx=scale, fy=scale)

    # 이미지 cleaning - 색깔이 전반적으로 서서히 바뀌도록 문대는거임
    image_blur = cv2.medianBlur(image, 7)  # cv2.GaussianBlur(image, (7,7), 0)
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)  # hsv 로 바꾸는 이유는? 좀 공부해야겠네...

    # 컬러 레인지로 필터 걸어서 잡아내기
    min_red = np.array([0, 100, 80])
    max_red = np.array([10, 256, 256])

    mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)

    # 밝은 영역 (?) 마스트 만들기
    min_red2 = np.array([170,100,80])
    max_red2 = np.array([100,256,256])

    mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)

    # 마스크 두개 합쳐서 연결해서 보도록 하기
    mask = mask1 + mask2


    # 세크멘테이션 (?)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)

    # 가장 큰놈만 찾기
    big_strawberry_contour, mask_strawberries = find_biggest_contour(mask_clean)

    # 마스크를 이미지에 오버레잉하기
    overlay = overlay_mask(mask_clean, image)

    # 가장 큰놈 놈에다가 동그라미 치기
    circled = circle_contour(overlay, big_strawberry_contour)

    show(circled)

    # 색깔 스킴 돌려놓기
    bgr = cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR)

    return bgr


if __name__ == '__main__':

    file = expanduser(r'~\pictures\strawberry.jpg')
    image = cv2.imread(file)
    print(image.__str__)
    result = find_strawberry(image)

    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



    vedio = expanduser(r'~\downloads\videoplayback.mp4')
    cap = cv2.VideoCapture(vedio)
    while True:
        ret, frame = cap.read()
        res = find_strawberry(frame)
        cv2.imshow('frame', res)

        k = cv2.waitKey(1) & 0xFF
        if k == 27: break

    cv2.destroyAllWindows()

