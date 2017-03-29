import cv2
import numpy as np

def drawing():
    img = np.zeros((512, 512, 3), np.int8)

    cv2.line(img, (0,42), (335, 512), color=(117, 136, 169), thickness=5)
    cv2.rectangle(img, (62, 152), (552, 25), (183, 95, 109), 30)
    cv2.circle(img, (24, 373), 152, (65, 28, 56), thickness=-1)   # -1 로 thickness 값 주면 안에까지 색채워줌

    # 원주, (장축, 단축), 시작각, 끝각, 전체각, 색깔, 띡
    cv2.ellipse(img, (186, 298), (201, 50), 0, 60, 270, (45, 39, 64), -1)

    # 폰트 넣기
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, 'by Paul', (106, 456), font, 3, (138, 111, 65), 3)

    # ploygon 글릴때는 int32 로 값 넘겨줘야함
    pts = np.array([[10,75],[210,30],[70,320],[50,110]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (223, 82, 54), thickness=10)

    cv2.imshow('drawing', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    drawing()