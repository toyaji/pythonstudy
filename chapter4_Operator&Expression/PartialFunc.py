def foo(x, y, z):
    return x + y + z

from functools import partial

f = partial(foo, 1, 2)
# partial() 함수는 다른 함수의 인수들 중에 일부만을 받아서 하나의 객체로 묶어서 가지고 있음

print(f(3))
# 추가로 마지막 인자만 들어오면 정상적으로 함수가 실행됨
