# 팩토리얼

def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

# 재귀 함수는 기존 함수를 닫고 새로 하는게 아니라서 함수를 여러개 계속 스택에 쌓다보니 깊이의 한계를 기본 설정해 둠
# 파이썬은 1000 이 재귀함수의 최대 깊이로 기본 설정되어 있고 변경하려면 변경메서드 써야함


import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(1001)

print(sys.getrecursionlimit())

# c = factorial(1001)

#  재귀한도 넘어가면 RuntimeError 발생함
#  파이썬은 tail-recursion Optimization 같은 기능을 제공하지 않아 ㅠ 재귀는 잘못쓰면 시스템 뻗는 원인될듯...
#  재귀 관련 참고 사이트 : http://hanmomhanda.github.io/2015/07/27/%EC%9E%AC%EA%B7%80-%EB%B0%98%EB%B3%B5-Tail-Recursion/


def flatten(lists):
    for s in lists:
        if isinstance(s, list):
            flatten(s)
        else:
            print(s, end=" ")

items = [[1, 2, 3], [4, 5, [5, 6]], [7, 8, 9]]
flatten(items)
print()

# 여기서 프린트를 yield 로 바꾸면 정상적으로 작동을 하지 않음 왜냐면 생성기만 계속 만들뿐이라서...
# 그래서 재귀 돌아가게 하려면 아래처럼 반복문 하나 더 넣어야함

def genflatten(lists):
    for s in lists:
        if isinstance(s, list):
            for item in genflatten(s):
                yield item
        else:
            yield s

a = genflatten(items)
print(a.__next__())
print(a.__next__())



#  decorator를 재귀함수에 사용하는 경우엔 내부 재귀함수 호출이 모두 래핑됨


