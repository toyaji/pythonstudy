# 공유 메모리 사용하여 다른 프로세스에 전해주는 예

import multiprocessing

class FloatChannel(object):
    def __init__(self, maxsize):
        self.buffer = multiprocessing.Array('d', maxsize)          # 'd' : double
        self.buffer_len = multiprocessing.Value('i')               # 'i' : singed int
        self.empty = multiprocessing.Semaphore(1)                  # 세마포어 : https://namu.wiki/w/%EC%84%B8%EB%A7%88%ED%8F%AC%EC%96%B4
        self.full = multiprocessing.Semaphore(0)

    def send(self, values):
        self.empty.acquire()                  # 버터가 비어야 진행함
        nitems = len(values)
        self.buffer_len = nitems
        self.buffer[:nitems] = values
        self.full.release()                   # 버퍼가 가득참을 알려줌

    def recv(self):
        self.full.acquire()                   # 버퍼가 가득 차야 진행함
        values = self.buffer[:self.buffer_len.value]
        return values

# 성능 테스트 부분
def consume_test(count, ch):
    for i in range(count):
        values = ch.recv()

def producer_test(count, values, ch):
    for i in range(count):
        ch.send(values)


if __name__ == '__main__':
    ch = FloatChannel(100000)
    p = multiprocessing.Process(target=consume_test, args=(1000, ch))
    p.start()

    values = [float(x) for x in range(100000)]
    producer_test(1000, values, ch)
    print("Done")
    p.join()