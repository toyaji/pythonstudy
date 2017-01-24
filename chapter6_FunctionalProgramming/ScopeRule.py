# 함수 실행 시 새로운 '지역 네임스페이스' 형성됨
# 변수 이름 해석시, 지역네임스페이스 -> 전역네임스페이스(모듈) -> 내장네임스페이스 순서로 인터프리터가 찾아들어감
# 그래도 없으면 NameError


a = 42; b =37

def foo():
    global a
    a = 13
    b = 0

foo()

print(a, b)

# 함수 내에서 선언된 변수는 지역변수로 함수 안에서만 작동하고 전역인 함수와 이름같아도 전혀 별개임


def countdown(start):
    n = start
    def display():
        print('T-minus %d' % n)
    def decrement():
        nonlocal n      # 중첩함수에서 바깥쪽 함수의 변수를 변경하려면 nonlocal 선언해야지만 가능함
        n -= 1
    while n > 0:
        display()
        decrement()



# 지역변수 선언안하고 그냥 쓰면 UnboundLocalError 발생함
