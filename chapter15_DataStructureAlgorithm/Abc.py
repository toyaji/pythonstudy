# 추상 기반 클래스 정의를 위한 메타클래스와 장식자 있음

import abc

# 추상클래스 설정하는 방법
class Stackable(metaclass=abc.ABCMeta):
    pass

"""
추상클래스 만드는 이유:
1. abstractmethod 와 abstractproperty 장식자를 이용해서 파생클래스에서 반드시 구현을 해야지 인스턴스 생성이 가능하게 강제할 수 있음
2. register(subclass) 메서드가 있어서 논리적으로 하위클래스를 등록하면 isinstance() 테스트 가능
3. __subclass__(cls, subclass) 를 추가로 정의하면, 서브클래스이면 True 아니면 Fasle 정보 없으면 NotImplemented 예외 발생
"""

from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod, abstractstaticmethod

# 추상기반 클래스 및 추상메서드와 프로퍼티 생성
class Stackabler(metaclass=ABCMeta):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractproperty
    def size(self):
        pass

# 상속하는 클래스
class Stack(Stackabler):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# 위에 상속받아서 설정했지만, 여전히 프로퍼티 없기때문에 프로퍼티 해줘야만 인스턴스 생성가능
class CompleteStack(Stack):
    @property
    def size(self):
        return len(self.items)


s = CompleteStack()
s.push("foo")
print(type(s))
print(s.size)