"""
. : 줄바꿈 외에 모든 문자
^ : 문자 시작
$ : 문자열 끝
... 너무 많아... 필요할때 찾아보도록   http://devanix.tistory.com/296  책보다 정리 잘됨
"""

# 정규표현식 다루는 모듈
import re

# 해당 정규 표현식을 객체로 컴파일함
rex = re.compile(r'(?P<mein>\d{6}[-]\d{7})')

# 문자열에서 알파벳 숫자에 외에 역슬래시 붙은 문자열로 반환
s = "Rehex Expression is not eeeasy"
print(re.escape(s))

# 문자열에서 해당 패턴 맞는 애들 리스트로 반환
l = re.findall(r'[a-z].\w', s)
print(l)

# findall 과 같지만 iter 로 반환
i = re.finditer(r'[a-z].\w', s)
print(next(i))

# 문자열의 시작 부위에서 매칭여부 확인하여 성공시 매칭 오브젝트 반환
m = re.match(r'[A-Z]\S+', s)
print(m)

# 문장안에서 첫번째 매칭 찾음
s1 = """Aggregates are calculated as weighted averages of available data for each time period.
Select an appropriate weight variable (GNI, population, GDP, exports, imports, labor
force or land area) from the Weight Indicator box, as shown above."""

ser = re.search(r'[A-Z]{3}', s1)
print(ser)

# 패턴이 나타나는 곳을 기준으로 분할
li = re.split(r'[.]\s', s1)
print(li)

# 패턴의 치환
ch = re.sub(r'(?P<a>\s[a])', r'\g<a>AAAAAAAA', s1)
print(ch)

# 정규식 객체 함수
print(rex.groupindex)             # 안에서 이름줘서 그룹 정의한 놈들 딕셔너리로 반환

print(rex.pattern)                # 패턴 반환

