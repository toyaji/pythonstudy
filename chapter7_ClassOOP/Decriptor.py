class TypedProperty(object):
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = type() if default is None else default

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default) if instance else self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

class Foo(object):
    name = TypedProperty("name", str)
    num = TypedProperty("num", int, 42)
# 클래스 수준에서만 기술자의 인스턴스를 생성할 수 있음(?)

f = Foo()
a = f.name
f.name = 'Guido'
del f.name

# __get__, __set__, __delete__ 함수를 정의 해줌으로써 속성값 설정해주려고 하거나 삭제하려고 할때 작용하는 방법 커스터마이징 할 수 있음
# 생각보다 이건 괘 복잡하네..ㅠㅠ