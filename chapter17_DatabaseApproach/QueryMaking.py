import psycopg2 as pg
import pandas as pd

c = pg.connect(host='localhost', database='dvdrental', port=5433, user='postgres', password='1234')
cur = c.cursor()


tab = 'customer'
col = 'first_name'
adr = 20

# 쿼리 쓸때 위에처럼 변수 설정하고 스트링 포맷으로 넣어서 가져오는 경우 가장 많음  - 그런데 문자열 변수 주게 되면 위험함!
cur.execute("select * from %s WHERE %s='Nancy' or address_id=%d" % (tab, col, adr))

# 모듈마다 다른 방식 쓰긴 하지만 문자열 포맷 아닌 자리표시자 사용함 - 아래는 예시일뿐
# cur.execute("select * from customer WHERE last_name=? or address_id=?", ('Thomas', 35))

cur.close()
c.close()