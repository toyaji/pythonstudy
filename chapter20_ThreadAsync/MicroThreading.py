# 작업 스케쥴러와 함께 생성기나 코루틴을 사용하여 다중 스레딩 구현하는 방법...

def foo():
    for n in range(5):
        print("I'm foo %d" % n)
        yield

def bar():
    for n in range(10):
        print("I'm bar %d" % n)
        yield

def spam():
    for n in range(7):
        print("I'm spam %d" % n)
        yield

# 작업 큐 생성하고 추가
from collections import deque
tasqkqueue = deque()
tasqkqueue.append(foo())
tasqkqueue.append(bar())
tasqkqueue.append(spam())

# 작업 돌아가면서 수행
while tasqkqueue:
    task = tasqkqueue.pop()
    try:
        # 다음 yield 까지 실행하고 다시 큐에 넣기
        next(task)
        tasqkqueue.appendleft(task)
    except StopIteration:
        pass