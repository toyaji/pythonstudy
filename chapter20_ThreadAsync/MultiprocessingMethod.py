# 하위 프로세스에서 작업수행, 데이터 교환 및 공유, 다양한 형식의 동기화 지원 모듈

import multiprocessing
import time

# 함수를 별도 프로세스로 실행하는 샘플 - 프로세스 하나로 15초에 한번씩 시간 찍어줌...
def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(15,))
    p.start()