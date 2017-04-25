from collections import deque
import numpy as np
import argparse
import imutils
import cv2

# 파싱 옵션 만들기
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="Path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="Max buffer size")
args = vars(ap.parse_args())

# 컬러 레인지로 필터 걸어서 잡아내기
min_red = np.array([0, 100, 80])
max_red = np.array([10, 256, 256])

# 밝은 영역 (?) 마스트 만들기
min_red2 = np.array([170, 100, 80])
max_red2 = np.array([100, 256, 256])

pts = deque(maxlen=args['buffer'])

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 빨간색 마스크 만들기
    mask1 = cv2.inRange(hsv, min_red, max_red)
    mask2 = cv2.inRange(hsv, min_red2, max_red2)
    mask = mask1 + mask2

    # 마스크에 opening Morphology 로 노이즈 문데기
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    kernel = np.ones((5,5), np.int8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # contour 찾기
    cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]))