# 먼저 알아둬야할 것은 우리가 프로그램을 실행하면
# 파이썬은 모든 function call 하고 매개변수, 지역변수에 대한 정보를 'Stack Frame' 이라고 하는 곳에 담아둠
# 그러다가 이게 프로그램이 돌다가 멈추면 이거를 뒤져서 어디서 멈췄는지 정보를 보여줌
# 이 Stack frame 은 메모리의 Stack 이라고 하는 곳에 위치함

import inspect

# 현재 프레임 불러오는 currentframe 이 inspect 모듈에 있음

def B():
    outerfram = inspect.currentframe().f_back
    functionname = outerfram.f_code.co_name
    return  "caller is {0}, and name is {1}".format(outerfram, functionname)


print(B())
