a = 10
def foo(x=a):
    return x

a = 5
print(foo())
# 함수를 정의하는 시점에 매개변수 값은 정해져버림. 이후에 해당 변수 고쳐도 함수의 매개변수값은 변하지 않아

def foo(x, items=[]):
    items.append(x)
    return items

# 함수에 리스트처럼 변경가능한 객체를 기본으로 넣는 경우 아래처럼 연달아 다른 정보 보여줄 가능성이 있음
print(foo(1))
print(foo(2))
print(foo(3))

def foo(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

# 요렇게 하면 이전 값 가져오는 것 방지할 수 있음


def foo(w, x, y, z):
    pass

foo('hello', 10, z=[1, 2], y=22)
foo('3', 22, w=13, y=1)   # 위치인수랑 키워드 인수 섞어서 쓰는 경우 여기서처럼 위치에 여러개 대입대는 것으로 인식해서 TypeError 날 수 있음