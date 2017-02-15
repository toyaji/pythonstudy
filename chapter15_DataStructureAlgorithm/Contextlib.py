# with 문과 함께 사용할 컨텍스트 관리자 및 장식자, 유틸리티 함수 제공
import contextlib


# 생성기 함수를 가지고 컨텍스트 관리자를 만드는 장식자 - with 문으로 함수 불러오는 경우, yield 직전까지 셋팅됨
@contextlib.contextmanager
def foo():
    try:
        for i in range(10):
            yield i**2
    except Exception as e:
        e.with_traceback()


with foo() as f:
    print(f)
