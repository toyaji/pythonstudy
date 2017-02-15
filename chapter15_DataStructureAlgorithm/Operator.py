# 연산자 함수 - 역호출이나 람다로 익명함수 정의향 되는 경우에 주로 사용됨


# 예시 - timeit 은 시간측정하는 함수
from timeit import timeit
t = timeit("functools.reduce(operator.add, a)", "import operator, functools; a = range(100)")
print(t)

t1 = timeit("functools.reduce(lambda x,y: x + y, a)", "import operator, functools; a = range(100)")
print(t1)

# 위에 두 경우 비교해보면 거의 두배 차이 나는거 볼 수 있음


