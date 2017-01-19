
# fucntion
def foo(x, y):
    "plus calcurator"
    return x + y

f = foo(3,4)

print(str.__name__)
print(foo.__doc__)


# method - 총 3 종류로 나누어짐. 인스턴스메서드, 클래스메서트, 스태틱메서드
class Foo(object):
    def instance_method(self, args):
        pass
    @classmethod
    def class_method(cls, arg):
        pass
    @staticmethod
    def static_method(arg):
        pass

f = Foo()
meth = f.instance_method
meth(20)  # 이미 인스턴스를 생성하고 여기에 딸려서 만들어졌기 때문에 인스턴스 자리에 따로 넣을 필요가 없음

umeth = Foo.instance_method  # () 없이 입력하면 메서드 자체를 변수에 바인딩 시킬 수 있음
umeth(f, 10)  # 메서드 묶을 때 인스턴스를 넣지 않아서 여기서 꼭 넣어주어야함

print(meth.__class__)
print(umeth.__repr__())

