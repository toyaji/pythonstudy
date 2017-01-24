# 파이썬 함수는 1급 객체로 다른 함수의 인자로 될수 있고, 자료 구조 안에도 들어갈 수 있고, 함수의 반환값이 될수도 있음

def callf(func):
    return func()

x = 37
def helloworld():
    print('Hello World. x is %d' % x)

callf(helloworld)


# 함수를 구성하는 문장과 실행환경을 함께 묶은 것을 클로저(closure) 라고 부름

print(helloworld.__globals__)
print()

# 모든 함수는 자신이 정의된 전역 네임스페이스를 가리키는 __global__라는 속성을 가짐


from urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get

# 중첩 함수 사용시에는 클로저는 내부 함수 실행을 위한 전체 환경을 담음
# laze evaluation or delayed evaluation 이라고 불리는 코드 작성 법인데,
# 클로저를 이용해서 객체 생성시점에는 안에 내용이 돌아가지 않고 이걸 변수에 할당하는 순간에 내부 함수가 돌아가도록 하는 방법임

python = page("http://www.python.org")  # 이 시점에 url 잡아서 객체만 생성함
pydata = python()   # 요 시점에 get() 이 돌아가서 리턴값 던져줌

print(python.__closure__)
print(python.__closure__[0].cell_contents)  # python 변수 선언시 해당 함수에 관련된 네임스페이스 및 정보를 담고 있음


def countdown(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        return r
    return next

next = countdown(10)
while True:
    v = next()
    print(v)
    if not v: break  # v = 0 이면 false 되니까...