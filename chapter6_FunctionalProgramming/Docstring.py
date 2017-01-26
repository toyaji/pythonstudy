def fibonacci(n):
    """Compute fibonacci n."""
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci.__doc__)


def wrap(func):
    def call(*args, **kwargs):
        return func(*args, **kwargs)
    call.__doc__ = func.__doc__               # 요 부분 없으면 장식자 사용시 문서화문자열이나 이름 못가져옴
    call.__name__= func.__name__
    return call


@wrap
def factorial(n):
    """Compute n factorial"""
    if n <= 1: return 1
    else: return n * factorial(n - 1)


help(factorial)



# 요런 문제 쉽게 해결하는 방법이 있는데 fucktool 모듈 임포트해서 wraps장식자 쓰는법임

from functools import wraps

def wrap(func):
    @wraps(func)
    def call(*args, **kwargs):
        return func(*args, **kwargs)
    return call