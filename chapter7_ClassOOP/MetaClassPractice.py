class TypedProperty(object):
    def __init__(self, type, default=None):
        self.name = None                       # 기술자의 네임속성을 자동으로 설정해주는 거를 메타로 만들 예정임
        self.type = type
        if default: self.default = default
        else: self.default = type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


# 메타 클래스 정의 부분, slots 를 이용한 인스턴스 명 자동 넣어줄 규칙 만들어줌
class TypedMeta(type):
    def __new__(cls, name, bases, dict):
        slots = []
        for key, value in dict.items():
            if isinstance(value, TypedProperty):
                value.name = "_" + key
                slots.append(value.name)
        dict['__slots__'] =  slots
        return type.__new__(cls, name, bases, dict)


class Foo(metaclass=TypedMeta):
    name = TypedProperty(str)
    num = TypedProperty(int, 42)

print(Foo.__dict__)
print(Foo._name)