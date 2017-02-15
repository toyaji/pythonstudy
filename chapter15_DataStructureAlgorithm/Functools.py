from functools import reduce

l = [1, 2, 3, 4, 5]

def foo(x, y):
    return x*y

# 앞에 있는 함수에 iter 를 집어넣어서 나온 결과값하고 다음뒤에 값을 다시 실햄하. 주어지는 함수는 반드시 인수 2개 받아야함
# 함수를 누적하는 효과있음
r = reduce(foo, l)
print(r)


# 장식자 만들때 쓰이는 녀석들

from functools import wraps

def debug(func):
    # wrapper 와 wrapped 를 받아서 속성을 복사해줌 - 기본적으로 __name__, __module__, __doc__ 있음
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("Calling %s" % func.__name__)
        r = func(*args, **kwargs)
        print("Done calling %s" % func.__name__)
    return wrapped

@debug
def add(x, y):
    return x+y

a = add(10, 20)