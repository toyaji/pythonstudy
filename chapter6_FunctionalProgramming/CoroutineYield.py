def receiver():
    print("Ready to receive")
    while True:
        n = (yield )
        print("Got %s" % n)

# 위에 함수처럼 yield 를 받아오는 구조를 코루틴(coroutine)이라고 함

r = receiver()
r.__next__()       # yield 직전까지 먼저 진행함. 받을 준비됨

# send() 함수를 이용하여 코루틴 돌리기 시작함

r.send(1)
r.send(2)
r.close()


# 코루틴 돌리기 전에 next 던져야 되는 거 잊어버리기 쉽기 때문에 아래처럼
# 장식자를 하나 만들어서 next 를 자동으로 던지도록 설정하면 편리함

def coroutine(func):
    def start(*args, **kwargs):
        g =func(*args, **kwargs)
        g.__next__()
        return g
    return start


@coroutine
def receiver():
    print("Ready to receive")
    try:
        while True:
            n = (yield )
            print("Got %s" % n)
    except GeneratorExit:
        print("Receiver done")


r = receiver()
r.send("Hello World")
# r.throw(RuntimeError, "You're hosed!")

r.close()

# r.send(10)
# close() 이후에 값 전달하면 StopIteration 에러 발생함


# 코루틴 입력값 받자마자 결과값 토해낼 수 있도록 설정하는 방법

@coroutine
def line_splitter(delimiter=None):
    print("Ready to split")
    result = None
    while True:
        line = (yield result)           # 요기서 result 를 바로 돌려줌
        result = line.split(delimiter)

l = line_splitter(',')
print(l.send("a,b,c,d"))