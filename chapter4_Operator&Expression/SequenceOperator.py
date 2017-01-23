import decimal

a = [3, 5, 4, 6, 7, 7, 2]

s = sum(a, decimal.Decimal(10))  # sum 함수에 인자를 주어서 초기값을 지정할 수 있음
ss = sum(a)


print(s)
print(ss)

a[2:3] = [20, 30]

print(a)

a[1::2] = [10, 10, 10, 10]  # 대입하려는 숫자 안맞으면 넣을 수 없고 'ValueError' 일어남

print(a)

if 'c' > 'a' :
    print(a)


