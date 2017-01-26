enable_tracing = True  # 요 전역변수 하나라 껐다 켰다 함으로써 전체 데코레이터를 작동시킬지 말지 결정할 수 있게됨
if enable_tracing:
    debug_log = open("debug.log", "w")

def trace(func):
    if enable_tracing:  # 중첩함수를 이용해서 데코레이터 작동여부를 전역변수로 토스하는 역할 하는거임
        def callf(*args, **kwargs):
            debug_log.write("Calling %s: %s, %s\n" % (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            debug_log.write("%s returned %s\n" % (func.__name__, r))
            return r
        return callf
    else: return func

@trace
def square(x):
    return x*x

def square(x):
    return x*x
square = trace(square)


# 아래 두 가지는 같은 결과 가져오는 거임
# 장식자의 주 목적은 다른 함수나 클래스를 포장하는 것이 주목적임 (Wrapper)


"""
@event_handlers
@trace
def grok(x):
    return

grok = event_handlers(trace(grok))
"""
# 위에랑 아래랑 같은 방식으로 작동함
# 장식자 여러개 가능하며 여러개 하는 경우 순서대로 랩핑할걸로 보면됨


event_handlers = {}
def eventhandler(event):
    def register_fuction(f):
        event_handlers[event] = f
        return f
    return register_fuction

# 처음에 함수 요런식으로 중첩으로 정의하는 이유는 클로져를 통해서 처음에 장식자에 인수 받을 때는 함수객체만 생성하고
# 이후에 랩핑하고 있는 안에 함수 돌때 실제로 내부 함수가 실행되도록 하기 위한 아주 지능적인 방법임 ㅎ


@eventhandler('BUTTON')
def handle_button(msg):
    ...

# 장식자도 인수 받을 수 있음. 이 경우에 인수받아서 장식자를 먼저 호출하고 그 다음에 아래 함수를 넣어서 돌리는 형식임

def foo(object):
    return object

@foo
class Bar(object):
    def __init__(self, x):
        self.x = x

# 클래스에 장식자 달려면 해당 장식자가 반드시 클래스 객체를 반환해야함 클래스 받아서 함수를 반환하거나 하면 에러남