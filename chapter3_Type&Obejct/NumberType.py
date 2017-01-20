from fractions import Fraction

# 유리수 연산을 위한 모듈안에  fraction 클래스 필요함.

x = Fraction('3/29') # 대,소문자 구별하고 '' 콤마 찍어야함

# fraction 함수로 설정해야지만 유리수 모듈 쓸 수 있음

print(x.numerator)
print(x.denominator)



z = 1.4 + 2.34j

print(z.real)
print(z.imag)
print(z.conjugate())

y = 3.456
print(y.as_integer_ratio())
print(y.is_integer())  # ???
