# 멀티프로세스는 스레드와 달리 공유 객체를 지원하지 않음. 그런데, multiprocessing 모듈은 관리자 제어하에 공유 객체로 작업하는 방법 지원함

import multiprocessing
import time

# 전달된 이벤트에 알림이 올 때마다 d를 출력
def watch(d, evt):
    while True:
        evt.wait()               # 쓰레드의 event 객체에 있는 함수 - 이벤트 인스턴스가 true 가 될때까지 기다림
        print(d)
        evt.clear()              # 이벤트 플래그를 false 로 설정함

if __name__ == '__main__':
    # 공유 객체 생성하고 접근하는데 사용하는 대리자반환 관련 메서드 있는 클래스 객채 - Manager
    m = multiprocessing.Manager()
    d = m.dict()    # 공유 dict 생성
    evt = m.Event()  # 공유 event 생성

    # 사전 감시하는 프로세스 구동
    p = multiprocessing.Process(target=watch, args=(d, evt))
    p.daemon = True
    p.start()

    # 사전을 갱신하고 감시자에게 알림
    d['foo'] = 42
    evt.set()                    #  event 객체의 불린 값 true 로 변경
    time.sleep(5)

    d['bar'] = 37
    evt.set()
    time.sleep(5)

    p.terminate()
    m.shutdown()