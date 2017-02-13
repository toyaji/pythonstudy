# 파이썬은 float 타입에 IEEE 754 배정밀도 부동소수점 인코딩을 사용
# https://ko.wikipedia.org/wiki/IEEE_754

""" 문제는 이게 이진기수법 때문에 부동소수점 계산하면 미묘하게 숫자가 안맞음 ㅠㅠㅠ
    이거를 해결하기 위해서 있는 것이 바로 이 모듈임"""

import decimal

x = 3.4
y = 4.5

a = x * y
b = x / y

print(a, b)

# 데시멀로 객체 만들고
x = decimal.Decimal('3.4')
y = decimal.Decimal('4.5')

# 정밀도 조정해줌
decimal.getcontext().prec = 3

a = x * y
b = x / y

print(a, b)

# 단일 블록안에서만 정밀도 변경
with decimal.localcontext(decimal.Context(prec=10)):
    e = x * y
    f = x / y

print(e, f)


print(decimal.Decimal(42))
print(decimal.Decimal((1, (2, 3, 4, 5), -2)))   # 맨 앞에 0 이면 양수, 1이면 음수, 그 튀에는 숫자, 맨끝에는 십진단위
print(decimal.Decimal("-Infinity"))             # 음의 무한대
print(decimal.Decimal("NaN"))                   # 숫자아님  - sNaN 은 이후 계산에 사용시 예외발생


# decimal 객체는 int 나 float 객체 기능 거의 다 가지고 있고 추가 기능 있음

z = decimal.Decimal(2)

print(z.exp())     # 자연지스 e 의  z 제곱
print(z.ln())      # 자연로그
print(z.log10())   # 10 로그
print(z.sqrt())    # 제곱근