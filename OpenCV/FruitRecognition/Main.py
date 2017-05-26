import cv2
import numpy as np
import imutils


# 컬러 레인지로 필터
min_red = np.array([0, 100, 80])
max_red = np.array([10, 256, 256])

# 밝은 영역 (?) 마스크필터 만들기
min_red2 = np.array([170, 100, 80])
max_red2 = np.array([179, 256, 256])


def findFruit(camera=1, width=600):
    """카메라 번호 또는 동영상 경로를 입력하면
    빨간색 딸기를 찾아주는 함수

    findFruit(카메라 연결번호, 읽어온 화면 사이즈 재조정할 기준 폭)

    '코루틴으로 값 받으면 다시 while 한번 돌고 대기하는 형태로 작성됨'

    """
    cam = cv2.VideoCapture(camera)

    while True:
        grab, frame = cam.read()

        if not grab:
            print("카메라에서 들어오는 영상이 없습니다.")
            break
        # 사이즈 재조정 및 HSV 로 컬러 변경
        frame = imutils.resize(frame, width=width)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 마스크 2개 생성
        mask1 = cv2.inRange(hsv, min_red, max_red)
        mask2 = cv2.inRange(hsv, min_red2, max_red2)
        mask = mask1 + mask2

        # 몰폴로지로 문데서 노이즈 줄이기 - http://blog.naver.com/samsjang/220505815055
        kernel = np.ones((5,5), np.int8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # 컨투어 찾아내기
        cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

        if len(cnts) > 0:
            # 면적 제일 큰 녀석으로 .. 딸기 적정 수준 확인하려면  요걸로 Contour 의 크기를 가지고 얼마 정도 수준 되는 놈만 따는 걸로 셋팅 할 수 있겠네....!!!
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
        else:
            print("컨투어를 찾지 못하는것 같습니다!!")

        circled = cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

        # 중앙에 정사각형 그리기 - 타겟지역
        h = int(frame.shape[0]/2)
        w = int(frame.shape[1]/2)

        cv2.rectangle(frame, (w-100, h-100), (w+100, h+100), (0, 255, 0), 2)

        #중심점에서 얼마나 떨어져 있나 찾아내기
        M = cv2.moments(c)
        cx, cy = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        distance = (w-cx, h-cy)

        #타겟지역 안에 컨투어 들어왔는지 확인하기
        lmost = tuple(c[c[:, :, 0].argmin()][0])
        rmost = tuple(c[c[:, :, 0].argmax()][0])
        tmost = tuple(c[c[:, :, 1].argmin()][0])
        bmost = tuple(c[c[:, :, 1].argmax()][0])

        if lmost[0] in range(w-100, w+100) and lmost[1] in range(h-100, h+100) and \
            rmost[0] in range(w - 100, w + 100) and rmost[1] in range(h - 100, h + 100) and \
            tmost[0] in range(w - 100, w + 100) and tmost[1] in range(h - 100, h + 100) and \
            bmost[0] in range(w - 100, w + 100) and bmost[1] in range(h - 100, h + 100):

            cv2.putText(frame, 'OK', (w-65, h+30), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 255, 255), 2)

        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFFc
        if key == ord('q'): break

        #yield distance
        #nextFlag = (yield )


if __name__ == '__main__':
    findFruit(0)