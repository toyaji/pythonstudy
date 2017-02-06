# 파이썬 3 에는 str 와 bytes 타입이 각각 따로 있음
# 각각 타입에 메소드 encode 와 decode 가 각각 있음


a = bytes(10)
b = str(10)

c = a.decode(encoding='utf-8', errors='ignore')
d = b.encode(encoding='ascii', errors='replace')

# 에러 옵션따라 해당 문자열 없는 경우에 처리방법 달라짐. 기본은 'strict' : UnicodeError 발생시킴
print(c, d)
