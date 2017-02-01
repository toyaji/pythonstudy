# 파이썬에 복소수 계산하는기능 이미 있지만 연산자 재정의 한번 해보기 위해 만드는거임

class Complex(object):
    def __init__(self, real, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self):
        return "Complex(%s, %s)" % (self.real, self.imag)

    def __str__(self):
        return "(%g+%gj)" % (self.real, self.imag)

    # self + other 을 정의하는 방법임
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # 역피연산자 정의
    def __radd__(self, other):
        return Complex(other.real + self.real, other.imag + self.imag)

    def __rsub__(self, other):
        return Complex(other.real - self.real, other.imag - self.imag)



c = Complex(2,3)

print(c + 4.0)
print(4.0 + c)

# 역피 연산자 정의 없이 맨 처음 주어진 인자값이 복소수가 아니면 에러가 나버림. 내장 부동소수점이 Complex 를 모르니까. 연산 정의가 없는거임
# 이런 경우를 위하여 '역피연산자' 를 정의하는 거임

