import inspect

# 속성, 문서화, 문자열, 소스 코드, 스택 프레임 등 라이브 파이썬 관련 정보 수집을 위하 모듈

frame = inspect.currentframe()   # 현재의 스택 프레임

a = inspect.getclasstree([bytes, int, bool])   # 여러 클래스 집어넣으면 상속관계 리스트로 돌려줌
print(a)

print(inspect.getcomments(str))   # 주석 가져옴 없으면 None

print(inspect.getfile(inspect))   # 해당 객체 있는 파일명 반환

print(inspect.getargvalues(frame))  # 프레임에 주어진 인수 값들 튜플로 반환

def foo(x):
    return x

print(inspect.getargspec(foo))     # 함수주면 인수값들 튜플로 반환      /// 이제 안쓰는듯?

print(inspect.getframeinfo(frame))  # 프레임 정보 Traceback 보여줌

c = foo(10)

print(inspect.getmembers(c))   # 해당 객체의 모든 멤버 소환 보통 __dict__에 정의되어 있는 반환

print(inspect.getmodule(frame)) # 오브젝트 정의된 모듈 반환

print(inspect.getmoduleinfo(r'C:\Users\user\Anaconda3\lib\inspect.py'))
# 모듈 경로 넣으면 관련 정보 보여줌         /// 이제 안쓰는듯?

print(inspect.getmodulename(r'C:\Users\user\Anaconda3\lib\inspect.py'))   # 모듈명

print(inspect.getsourcefile(foo))  # 모듈, 클래스, 함수의 소스파일명

class cc(object):
    pass
print(inspect.isclass(cc))  # 클래이면 True 반환

print(inspect.isfunction(foo)) # 함수이면 True 반환

def gen(x):
    for i in range(x):
        yield i

g = gen(20)
print(inspect.isgenerator(g))   # 생성기 객체이면 True

print(inspect.isgeneratorfunction(gen))  # 생성기 함수이면 True

print(inspect.stack())  #getframeinfo 랑 차이 뭐지...??

