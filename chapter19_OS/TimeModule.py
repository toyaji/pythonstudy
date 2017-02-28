import time

# 운영체제 별로 epoch 타임 시작점이 다름 - 확인하는 방법
print(time.gmtime(0))

# 일광 절약 시간 (DST) 동안 사용할 시간대 - 현재 한국은 따로 없어서...
print(time.daylight)

# 지역 시간대
print(time.timezone)

# 지역 시간대 이름 하고 DST 이름 담은 튜플...깨지네..
print(time.tzname)

# 로컬 타임 담은 시간
print(time.localtime())
print(time.asctime(time.localtime()))

# 초로 나타내는 현재 cpu 시간
print(time.clock())

# epoch 시간을 UTC 시간으로 변환하여 struct-time 객체 반환
t = time.gmtime()
print(t)

# 시간 입력받아서 struct-time 객체로 만들어줌 - 9개 인자 다 줘야함... 쓸일없겠군...
t1 = time.mktime((1984, 11, 30, 22, 45, 2, 1, 46, 0))

# 호출 스레드를 n 초 동안 잠재움
time.sleep(5)

# 타임객체에 포맷팅 입힘
print(time.strftime('%B %Y %x'))

# 시간표현한 문자열을 파싱해서 타임객체로 반환
t2 = time.strptime('1999-12-10', '%Y-%m-%d')
print(t2)