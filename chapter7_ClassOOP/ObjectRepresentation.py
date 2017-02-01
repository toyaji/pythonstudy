# __dict__ 속성으로 인스터스의 고유 데이터를 딕셔너리로 볼 수 있음

from chapter7_ClassOOP.ObjectMemoryManagement import Account

a = Account('Guido', 1100.0)

a.number = 12345   # 인스턴스에 변화주거나 __dict__ 에 직접 변화줘도 인스턴스에 영향미침
print(a.__dict__)
print(a.__class__)   # 클래스에 연결된거 볼수있음

print(Account.__dict__.keys())   # 클래스의 사전에 가면 메소드가 다 들어있음


# __getatrr__ , __setatrr__ 로 속성값 검색해오는 방법 정의할 수 있음
# 기본적으로는 __getatrribute__는
# 1. 프로퍼티를 찾아보고  2. 내부 __dict__ 를 찾아보고 3. 클래스 사전을 찾아보고  4. 마지막으로 기반 클래스를 찾아봄
# 여기까지 찾지 못하면 다음으로 __getatrr__ 를 불러오는 형태임

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __getattr__(self, name):
        if name == 'area':
            return math.pi * self.radius
        elif name == 'perimeter':
            return 2 * math.pi * self.radius
        else:
            return object.__getatrr__(self.name)

    def __setattr__(self, name, value):
        if name in ['area', 'perimeter']:
            raise TypeError('%s is readinly' % name)
        object.__setattr__(self, name, value)