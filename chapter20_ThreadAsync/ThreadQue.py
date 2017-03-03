# 쓰레드에서 큐 사용하는 예시

import threading
from queue import Queue

class WorkerThrad(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.input_queue = Queue()

    def send(self, item):
        # 큐에다가 아이템 추가함, block 옵션 false 로 추가하면, 꽉차있으면 에러 띄움
        self.input_queue.put(item)
        # 큐에 모든 항목 제거될때까지 기다림
        self.input_queue.join()

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    # 해당 스레드 실행 시점에 돌아가는 부분이 run 이라서 반드시 구현해줘야함
    def run(self):
        if __name__ == '__main__':
            while True:
                item = self.input_queue.get()
                if item is None:
                    break
                print(item)
                # 항목처리가 다 됬다고 알려줌... 큐에 있는 항목당 한번만 실행해야함
                self.input_queue.task_done()
            # 완료. 표지 받음을 알리고 반환.
            self.input_queue.task_done()
            return

w = WorkerThrad()
w.start()
w.send('Hello')
w.send('World')
w.close()