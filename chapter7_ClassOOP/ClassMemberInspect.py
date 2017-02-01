class A(object): pass
class B(A): pass
class C(object): pass

a = A()
b = B()
c = C()

print(type(a))
print(isinstance(a, A))
print(isinstance(b, A))    # 상속 받은 경우에 True 값 반환함
print(isinstance(b, C))

print(issubclass(B, A))    # 하위 클래스 여부 물어보는 메서드 issubclass


# 만약에 여러 클래스를 그룹으로 묶어서 상호 같은 인스턴스가 같은지 보려면?
# __instancecheck__ 과 __subclasscheck__ 을 재정의해서 사용할 수 있음


class IClass(object):
    def __init__(self):
        self.implementors = set()

    def register(self, C):
        self.implementors.add(C)

    def __instancecheck__(self, x):
        return self.__subclasshook__(type(x))

    def __subclasscheck__(self, subclass):
        return any(c in self.implementors for c in subclass.mro())
    # any 의 경우에 set 을 돌아서 아이템 찾으면 True를 반환함


IFoo = IClass()
IFoo.register(A)
IFoo.register(C)

print(isinstance(A, IFoo))
print(isinstance(b, IFoo))