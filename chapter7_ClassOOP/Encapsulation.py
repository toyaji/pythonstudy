# 파이썬은 기본적으로 클래스의 모든속성과 메서드가 공개되어 있음
# 대신에 이름변형(name mangling) 을 통해서 캡슐화를 할 수 있음

class A(object):
    def __init__(self):
        self.__x = 3    # self._A__x 로 이름이 변형됨

    def __spm(self):
        pass

    def bar(self):
        self.__spm()   # A.__span() 만 실행됨. 파생클래스에서 사용하는 이름과 충돌을 막아주고 이 클래스에서만 쓸수있게 됨


class B(object):
    def __init__(self):
        A.__init__(self)
        self.__x = 37

    def __spam(self):
        pass