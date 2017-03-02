# 매니저 객체에 있는 일반적인 메서드 왜에 기타 객체를 공유 객체로 쓰기 위해서는...

import multiprocessing
from multiprocessing.managers import BaseManager

class A(object):
    def __init__(self, value):
        self.x = value

    def __repr__(self):
        return "A(%s)" % self.x

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value

    def __iadd__(self, value):
        self.x += value
        return self

class MyManager(BaseManager): pass
# 아래 메서드를 통해서 공유 객체에 대한 대리자 반환 메서드 생성... 말이 어려워..ㅠ
MyManager.register('A', A)


if __name__ == '__main__':
    m = MyManager()
    m.start()
    # 관리 객체 생성
    a = m.A(37)

    # 관리자 서버사 사용하는 주소 튜플로 반환
    print(m.address)

