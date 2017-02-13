import types

# 내장 타입관련 연산... 타입 자체를 만들고 하는 과정 커스터마이징 할 수 있음

# 코드 객체 생성... 들어가는 인자값 너무 많아서 직접 만들일 많지 않을듯... 상세 설명은 아래 링크로...
print('http://stackoverflow.com/questions/16064409/how-to-create-a-code-object-in-python')

def F(a,b):
    global c
    k=a*c
    w=10
    p=(1,"two",3)

print(F.__code__.co_argcount)
print(F.__code__.co_nlocals , F.__code__.co_varnames)
print(F.__code__.co_stacksize)
print(F.__code__.co_flags)
print(F.__code__.co_names)
print(F.__code__.co_consts)

# types.CodeType()