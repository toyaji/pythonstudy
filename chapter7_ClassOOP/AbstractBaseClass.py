from abc import ABCMeta, abstractmethod, abstractproperty

# abc : 추상화 관련된 모듈

class Foo(metaclass=ABCMeta):
    @abstractmethod
    def spam(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass


# 추상클래스는 바로 인스턴스 만들 수 없음

# f = Foo()


# 추상 클래스는 쓰는 이유는 하위클래스에서 반드시 구현되야 하는 메서드나 프로퍼티를 강제하기 위한 목적이 주요임

# 추상 클래스는 register() 로 기존 클래스를 등록하는 기능 제공함

class Grok(object):
    def spam(self, a, b):
        print("Grok.spam")

Foo.register(Grok)

print(issubclass(Grok, Foo))