import multiprocessing
import time

# 프로세스 클래스를 상속받아서 구현함
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(15)
    p1 = ClockProcess(3)
    p.start()
    p1.start()

    # 프로세스가 현재 실행중인 경우 true
    print(p.is_alive())

    # 프로세스의 인증키
    print(p.authkey)

    # 데몬 프로세스 여부 (데몬 : https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%AA%AC_(%EC%BB%B4%ED%93%A8%ED%8C%85)
    print(p.daemon)

    # 프로세스 이름
    print(p.name)

    # 프로세스의 정수 id
    print(p.pid)