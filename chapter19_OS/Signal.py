# 시그널 (타이머 만료, 데이터 도착 등 사용자 동작으로 프로그램에 전달되는 비동기 이벤트) 처리기 작성을 위한 모듈
# 주로 유닉스에서 사용함... 아래 예시도 안먹히네.. 윈도에서는..

import signal, socket

def handler(signum, frame):
    print('Timeout')
    raise IOError('Host not responding.')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
sock.connect('www.python.org', 80)
signal.alarm(0)