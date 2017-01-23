print('format %r' % 102394)  # repr() 의해 생성되는 것과 동일한 문자열생성
print('format %c' % 'c')   # 단일문자
print('format %E' % 102392394)  # 부동소수점으로 표현함

a = 42
b = 13.114959
c = "hello"
d = {'x' : 113, 'y' : 1.5429, 'z' : 'world'}
e = 209370189274977590129

print("a is %d" % a)
print("%10d %f" % (a, b))
print("%+010d %E" % (a,b)) # 앞에 영을 영으로 채워달라는 거임, 플러스 부호는 부호표시
print("%(x) - 10d %(y)0.3g" % d)  # 키나 맵을 넣으려면 () 괄호로 표시하면 됨.  - 부호는 왼쪽정렬 의미함
print("%*.*f" % (5,3,b)) # 포맷 설정할때 * 표시하면 해당 부분을 뒤에서 설정해주면됨
print("e = %d" % e)


stock = {
    'name' : 'GOOG',
    'share' : 100,
    'price' : 490.10
}

r = '%(share)d of %(name)s at %(price)0.2f' % stock   # 문자열 필드의 확장방법
print(r)

name = "Elwood"
age = 41
r = "%(name)s is %(age)d years old" % vars()  # vars() 함수 호출하면 호출 시점에 정으된 모든 변수를 담은 사전을 반환함
print(r)

c = "Hello %s %s"
c %= ("Month", "Python")  # 확장 대입 연산자를 사용할 수도 있음

print(c)
