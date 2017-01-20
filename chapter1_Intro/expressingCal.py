principal = 1000
rate = 0.05
numyear = 5; year = 1   # 한 줄에다가 이렇게 줄줄이 입력가능

while year < numyear:
    principal = principal * (1 + rate)
    print(year, principal)
    print()
    print("%3d %0.2f" % (year, principal))
    print()
    print(format(year,"3d"), format(principal, "0.2f")) # 하나씩 셋팅할때
    print()
    print("{0:3d} {1:0.2f}".format(year, principal))   # {} 콜론 앞에는 포맷 메서드에 전달된 인수 (?)

    year +=1

  # 줄바꿈 할때는 " \ " 역 슬래시 씀
if year == 5 and type(rate) == float \
             and not (principal < 400 or principal > 1000):
    print("I'll take it over")