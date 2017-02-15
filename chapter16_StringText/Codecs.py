# 문자 인코딩 관련 모듈 - 자바처럼 저수준에서 제공
import codecs

# 해당 인코딩 이름이 존재하는 검색, 없으면 LookupError 반환
try:
    codecs.lookup('utf-40')
except LookupError:
    print("이런 인코딩 값 없음!")


# 문자열 s 를 인코딩 하여 튜플로 반환 ( 뒤에 값은 길이 )
c = codecs.lookup('ascii')
s = 'We will encode this line'
t = c.encode(s)
print(t)

# 바아니러 객체 읽어오는 메서드
b = s.encode()
r = c.streamreader(b)
print(r.read(5))