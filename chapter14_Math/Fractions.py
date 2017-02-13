# 유리수 다루는 모듈
import fractions

f = fractions.Fraction(3, 4)
g = fractions.Fraction("1.75")
h = fractions.Fraction.from_float(3.1415926)

print(f)
print(g)
print(h)
print(f + g)
print(f * g)

# 가장 큰 분모 한계 설정하는 방법
print(h.limit_denominator(10))

# 두 수의 최대 공약수 보여주는 함수
print(fractions.gcd(10, 20))