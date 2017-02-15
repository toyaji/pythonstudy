# str.format() 연산과 관련하여 커스터마이징 필요한 경우에 string 모듈에 formatter 객체 이용할 수 있음

from string import Formatter

# 인스턴스 생성
f = Formatter()

# 포맷지정
sf = f.format("{name} is {0:d} old", 39, name="Dave")
print(sf)

# 포맷 스트링을 훑으면서 파싱 정보 튜플로 반환 : 결과값 - (literal text, field name, format spec, conversion(?))
fu = f.parse("{name} is {0:d} old")
print(next(fu))
print(next(fu))

#
print(f.get_field())