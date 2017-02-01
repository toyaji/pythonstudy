# 클래스 정의 자체도 한의 클래스인데, 클래스 객체를 생성하는 일을 메타 클래스라고 하는 특수 클래스에서 담당함

# 메타 클래스 지정하는 법
class Foo(metaclass=type):
    pass

# 메타 클래스 종류는 따로 지정하지 않으면 기반 클래스와 같도록 되고, 기반 클래스 없으면 전역변수로 __metaclass__ 찾음

# 아래 예시는 모든 메서드에 문서화문자열 doc 강제하는 메타클래스 정의 ...
class DocMeta(type):
    def __init__(self, name, base, attrs):
        for key, value in attrs.items():
            if key.startswith("__"): continue
            if not hasattr(value, "__call__"): continue
            if not getattr(value, "__doc__"):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self, name, base, attrs)

# 보통 이렇게 메타 클래스를 사용하기 위해서 중간에 기반 클래스를 하나 두는 경우가 많다는데... 이유는 모르겠음?
class Documented(metaclass=DocMeta): pass


class Foo(Documented):
    def spam(self, a, b):
        "spam does somthing"
        pass

# 위에서 정의한 메타 클래스 사용된 클래스에 만약에 docstring 없으면 바로 설정한 에러메시지 던져줌
a = Foo()