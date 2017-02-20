# 파이썬 타입하고 사용하려는 db 의 타입이 다른 경우 요거를 조정해줘야함

import psycopg2 as pg
import pandas as pd

c = pg.connect(host='localhost', database='dvdrental', port=5433, user='postgres', password='1234')
cur = c.cursor()

# 요런식으로 데이터베이스에 맞게 타입 캐스팅 해줘야함
# 문제는 지금 pg 같은 경우는... 하부에서 len() 값을 돌려주지 못하니까 에러 뜨는듯...
# 커스터마이징 해야되는데..c 로 만들어서 어려울듯...?
cur.callproc('last_day', pg.Timestamp(1999, 12, 31, 11, 30, 57))


pg.DateFromTicks()

cur.close()
c.close()