import time
import datetime

# 시간 관련 함수는 일단 이렇게 2가지 있는듯...

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)      # tm_year 이 아이들은 time 의 attr
    # tm_mday 날짜, tm_wday 요일, tm_yday 1월1일부터 몇째날인지
    # datetime.date(year, month, day) 인수 받아서 시간 값으로...(?)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(1967, 4, 9)
b = Date.now()
c = Date.tomorrow()

# 날짜 객체를 생성함
print(type(b))
print()
print(time.strftime("%Y %B %m %A", time.localtime()))