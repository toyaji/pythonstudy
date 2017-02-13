import decimal

# 반올림이나 정미리도 처럼 십진수 제어하기 위한 용도의 객체 임
# prec : 정밀도 숫자 객수, rounding : 반올림 설정, traps : 계산 중에 이벤트 발생시 예외 발생, flag :
c = decimal.Context(prec=15, rounding='ROUND_HALF_DOWN')

a = decimal.Decimal(10.45)
b = decimal.Decimal(0)

# 컨텍스트 객체의 신호(flag) 사용 예 : 예외처럼를 상속받아서 계층 구조로 만들어져서 예외처럼 처럼 사용할 수 있음
try:
    x = a / b
except decimal.DivisionByZero:
    print('Division by zero', '\n')

# 일반적으로 컨텍스트 객체 아래처럼 현재 쓰이는 놈 불러다가 특정부분 만져서 사용하는 형태로 쓰여짐
ctxt = decimal.getcontext()
print(ctxt, '\n')
x = a + b
print(ctxt.flags, '\n')
if ctxt.flags[decimal.Rounded]:
    print("Result was rounded")

ctxt.capitals = 0
ctxt.prec = 3        # 정밀도를 먼저 설정하고 그 다음에 계산을 해야함
print(x)
print(a + b)

# 현재 모든 플래스 초기화 (전부 false 로 반환함)
ctxt.clear_flags()
print(ctxt.flags)

# 설정된 컨텍스트를 기반으로 decimal 객체 만드는 방법
z = ctxt.create_decimal(a + b)
print(z)

#