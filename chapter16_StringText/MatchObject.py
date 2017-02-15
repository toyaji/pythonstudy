import re

s1 = """Aggregates are calculated as weighted averages of available data for each time period.
Select an appropriate weight variable (GNI, population, GDP, exports, imports, labor
force or land area) from the Weight Indicator box, as shown above."""

# 정규식 모듈에서 search 와 match 가 반환하는 인스턴스가 MatchObject 임.
ser = re.search(r'(?P<two>[A-Z]{3})\S(?P<blank>\s.)', s1)

# 정규 표현식 내에서 그룹명으로 결과 집어 나오는 방법
print(ser.group('two'))

# 모든 그룹에 대한 매칭 튜플 , 딕셔너리
print(ser.groups())
print(ser.groupdict())

# 그룹이 뽑은 아이들 색인의 처음과 끝 보여줌
print(ser.start('blank'))
print(ser.end('blank'))
print(ser.span('blank'))

# 매칭된 그룹의 마지막 인덱스 - 그룹이 2개라는 말 ?
print(ser.lastindex)

# 표현식의 마지막 그룹명
print(ser.lastgroup)

