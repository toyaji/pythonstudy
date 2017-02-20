import psycopg2 as pg
import pandas as pd

c = pg.connect(host='localhost', database='dvdrental', port=5433, user='postgres', password='1234')
cur = c.cursor()

# 저장된 프로시져를 이름명으로 해서 부르는 함수 - 현재 타입 에러남... 기본함수로는 타입캐스팅이 안되는듯...
# cur.callproc('inventory_in_stock',2016)

# 쿼리 날리는 거
cur.execute('select * from city')

# cur.executemany()  요거는 뒤에다가 변수를 매핑으로 넣어서 돌아가면서 쿼리 날리도록 하는 거임

# fetchmany() 연산에 사용될 기본 값 주는 정수..
print(cur.arraysize, '\n')

# 튜플로 현재 결과 집합에 대한 각열 정보를 제공함
print(cur.description, '\n')

# 줄 숫자
print(cur.rowcount, '\n')
city = cur.fetchmany(100)
df = pd.DataFrame(city)

print(df)

cur.close()
c.close()