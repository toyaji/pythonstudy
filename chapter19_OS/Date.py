# 날짜 관련 모듈

from datetime import date


# 연월일 날짜 표현
d = date(2017, 2, 20)
print(d)

# 오늘날짜
print(date.today())

# 타임스탬프에 해당하는 date 객체반환
import time
st = time.time()
print(date.fromtimestamp(st))

# 1년 1월 1일 로 부터 몇일지난 날 반환 ( ordinal 이라고 함)
print(date.fromordinal(794853))

# 표현가능한 날짜 범위
print(date.min, date.max)

# 객체 사이의 최소단위 표현 - 구지 필요없을듯...
print(date.resolution)

# 분해가능
print(d.year, d.month, d.day)

# 날짜를 튜플로 반환 - ( year, 몇째주인지, 무슨요일인지)
print(d.isocalendar())

# 포맷셋으로 반환
print(d.isoformat())

# 요일
print(d.isoweekday())

# 구성요소 대체
d = d.replace(day=23)

# 포맷 셋팅가능 - 요거는 연선자 좀 알아야함 : https://docs.python.org/2/library/time.html
print(d.strftime('%a %A %b %B %d'))

# 타임모듈에서 쓰기 좋게 튜플로 반환
print(d.timetuple())