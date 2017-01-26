import threading

lock = threading.Lock()
with lock:
    pass

#  with 들어갈때 뒤에 있는 obj.__enter__가 실행됨. 빠져나올때 obj.__exit__(type, value, traceback) 실행됨
#  흐름상 예외 없으면 변수는 모두 None 이고 중간에 끊기면 예외 관련 정보 담아나옴

class ListTransaction(object):
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.thelist[:] = self.workingcopy
        return False   # 리턴값이 False인 경우 발생한 예외가 컨텐스트 밖으로 전달됨 고로 자체적으로 정의해서 먼가 받을려면 false로 설정해야함


Items = [1, 2, 3]
with ListTransaction(Items) as working:
    working.append(4)
    working.append(5)

print(Items)

# 아래 형태로 실행하면 에러 일으키면서 __exit__ 의 type 값이 None이 아니게 됨 따라서 items 파일도 수정되지 않고 그대로임

try:
    with ListTransaction(Items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("We're hosed!")
except RuntimeError:
    pass

print(Items)

# 아래의 contextlib 의 contextmanager  Wrapper 를 이용하면 위에 클래스와 같은 기능하는 함수를 쉽게 만들 수 있음

from contextlib import contextmanager

@contextmanager
def ListTransaction(thelist):
    workingcopy = list(thelist)
    yield workingcopy    # __exit__ 실행시점에 yield 뒷 부분이 실행됨
    thelist[:] = workingcopy