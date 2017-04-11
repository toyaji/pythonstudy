import numpy as np
import cv2


def hsv_understand():
    blue = np.int8([[[255,0,0]]])
    green = np.int8([[[0,255,0]]])
    red = np.int8([[[0,0,255]]])

    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

    print('HSV for blue:', hsv_blue)
    print('HSV for green:', hsv_green)
    print('HSV for red:', hsv_red)

def tracking_vedio(vedio):
    try:
        print('Start Tracking')
        # img = cv2.imread()
        # 비디오 캡쳐로 쓸려면 아래 걸로 해야함
        cap = cv2.VideoCapture(vedio)

    except:
        print('Cannot Load Camera...')

    while True:
        # 이미지 프레임 읽어서 HSV 로 전환
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 색상 레인지 정의하는 부분
        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        # thresh 를 범위로 걸어서 마스크 만드는 방법임
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        # 비트 연산으로 원래 이미지 하고 걸러내기
        res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
        res3 = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow('Original', frame)
        cv2.imshow('Blue', res1)
        cv2.imshow('Green', res2)
        cv2.imshow('Red', res3)

        k = cv2.waitKey(1) & 0xFF
        if k == 27: break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    tracking_vedio(r'C:\Users\user\Downloads\v.mp4')