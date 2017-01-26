import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.area)
c.area

# 프로퍼티의 가장 큰 장점은 이게 attr 인지 func 인지 몰라도 모두 작동한다는 점이다
# area() 과 area 의 작동이 똑같이 된다. 다만, 속성값인줄 알고 값을 바꿀려고 하면 AttributeError 가 난다


class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):                    # 재정이 하려는 함수와 같은 이름으로 해야함
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")

# 프로퍼티를 이용한 속성값 설정 및 삭제 함수 정의 방법 ( 결국, 속성값을 함수처럼 표현하려고 하는 거기 때문에 필요함)

f = Foo("Guido")
n = f.name
f.name = "Monty"
print(f.name)
# f.name = 45
del f.name