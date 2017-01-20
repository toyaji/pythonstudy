a = [2, 3, 4, 5]
s = repr(a)  # 문자열 반환식으로 만들어줌
b = eval(s)  # 다시 리스트 처럼 val 로 만들어줌

print(a)
print(type(s))
print(b)
print(type(b))

