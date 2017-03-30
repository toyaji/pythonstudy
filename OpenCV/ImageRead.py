from os.path import expanduser, exists
import cv2


path = expanduser(r'~\downloads\figure-blueberry.jpg')

def handle_image(path):
    if exists(path) == False :
        print("파일이 존재하지 않습니다.")
        exit()

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # 윈도운 형태 설정 - 자동으로 맞출지, 아니면 조정하도록 해야할지 등
    cv2.namedWindow('Berry', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Berry', img)
    # 화면 띄운다음에 사용자가 키 누를때가지 기다림 - 0 으로 인자값 주면, 숫자주면 밀리세컨동안 띄움
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    handle_image(path)
