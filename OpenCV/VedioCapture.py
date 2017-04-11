import cv2
from os.path import expanduser

def vedio_handler(source=0):
    # 기본은 웹캠인데, source 넣어주면 해당 비디오 읽어옴
    cap = cv2.VideoCapture(source)
    print(cap.isOpened())           # 캡 열려있나 확인함 -> 안 열려있으면 cap.open() 하면 됨
    print(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 카메라 관련 세팅 값 가져오거나 설정할 수 있음
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    while True:
        # 이미지 제대로 읽었으면 ret 값이 true 가 됨
        ret, frame = cap.read()
        # 흙백으로 전환하는 객체
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def vedio_recoder(path):
    cap = cv2.VideoCapture(0)

    # 화소 셋팅하기
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)

    fps = 20.0
    heigth = int(cap.get(4))
    width = int(cap.get(3))
    fcc = cv2.VideoWriter_fourcc(*'DIVX')     # 윈도우는 DIVX 페도라는 XVID 코덱이 선호됨
    out = cv2.VideoWriter(path, fcc, fps, (width, heigth))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 0)
            # 파일에 출력하는 부분
            out.write(frame)
            cv2.imshow('frame', frame)

            # 20 프레임에서 0.05 초 씩 딜레이 줘야 속도 맞음.. 이거 참 신기하네...
            if cv2.waitKey(50) & 0xFF == ord('q'): break
        else: break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    file = expanduser(r'~\downloads\v.mp4')
    recordfile = expanduser(r'~\downloads\VideoEncoding.avi')
    vedio_handler()
    vedio_recoder(recordfile)