class Foo(object):
        pass


print(type(Foo))  # 클래스 만들면 type 이 'type' 인 객체로 생성됨
f = Foo()

print(f.__dict__)
print(f.__class__)

print(str.__dict__)  # dict 는 보통 관련 데이터를 담은 딕셔너리 반환함

