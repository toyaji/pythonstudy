# 날짜나 시간의 차이를 표현하는데 사용하는 객체

from datetime import timedelta

td = timedelta(days=1, seconds=15, microseconds=0.1234)
td1 = timedelta(days=2, seconds=35, microseconds=0.1234)


# timedelta 객체는 대부분이 연산자 지원함
td2 = td + td1
print(td2)
print(td * 7)

