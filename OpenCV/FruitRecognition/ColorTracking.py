import cv2
import numpy as np
from os.path import expanduser
import pandas as pd

def object_tracking(cam=0):
    cap = cv2.VideoCapture(cam)
    while True:
        ret, frame = cap.read()
        # 색깔 바꾸기
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 색상 범위 설정하기
        lower_red = np.array([130,50,50])
        upper_red = np.array([230,255,255])
        # 마스크 만들기
        mask = cv2.inRange(hsv, lower_red, upper_red)
        # 비트 연산으로 마스크랑 중첩시켜서 추출하기
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # 흑백으로 바꾸고 가우시안이랑 오쑤 입혀서 윤곽 확실히 잡아보자...
        bw = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        th3 = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 71, 70)

        cv2.imshow('frame', res)
        # col_info(bw)

        k = cv2.waitKey(1) & 0xFF
        if k == 27: break

    cv2.destroyAllWindows()


def col_info(frame):
    df = pd.DataFrame(frame)
    print(df.head())



if __name__ == '__main__':
    vedio = expanduser(r'~\downloads\strawberry.mp4')
    object_tracking(vedio)