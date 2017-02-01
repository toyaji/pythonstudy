# 메타클래스는 클래스가 생성되는 과정을 커스터마이징 하는게 목적이라면,
# 클래스 데코레이터는 클래스가 생성되고 난 후에 추가 작업을 주고 싶은게 목적임

# 레지스트리에 클래스 정보 등록하는 장식자
registry = {}
def register(cls):
    registry[cls.__clsid__] = cls     # 받아온 매개변수안에 선언된 변수 가져오는 방법임.`
    return cls

# 장식자 적용하는 방법
@register
class Foo(object):
    __clsid__ = "123-456"
    def bar(self):
        pass


print(registry)