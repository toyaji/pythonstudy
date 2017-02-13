# 약한 참조에 대한 지원 제공
import weakref

# 약한 참조 만드는 이유는 순환 참조로 인한 문제 해결하려는거임

class A: pass
a = A()

# 약한 참조 만드는 방법
ar = weakref.ref(a)

print(ar())
del a
print(ar())   # 참조 대상 삭제되면 None 반환

# 약한 참조 이용한 대리자 생성
Ar = weakref.ref(A)

print(weakref.getweakrefcount(A))  # 해당 객체 가리키는 약한참조 및 대리자

print(weakref.getweakrefs(A))      # 약한참조 리스트

print(weakref.WeakKeyDictionary().keyrefs()) # 키가 약하게 참조되는 사전을 생성함

print(weakref.WeakValueDictionary())   # 밸류가 약하게 참조되는 사전 생성


# 사용예시
_resultcache = {}
def foocache(x):
    if x in resultcache:
        r = _resultcache[x]()
        if r is not None:
            return r
    r = foo(x)


