from datetime import datetime, date, time

dt = datetime(2016, 12, 31, 23, 48, 30)

# 합쳐서 생성도 가능함
d = date(2017, 1, 1)
t = time(14, 11, 33)
dt1 = datetime.combine(d, t)
print(dt1)

# 현재 시간 및 시간대로 만들어옴
dt2 = datetime.now()
print(dt2)

# 현재 협성 세계시 반환 (UTC : Universal Time Coordinated)
dt3 = datetime.utcnow()
print(dt3)

# time, date 객체로 쪼갬
t1 = dt2.time()
d1 = dt2.date()


# 날짜 관련 객체는 일반 연산자 대체로 제공함
if t1 < t: print('Wow')