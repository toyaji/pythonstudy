import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/db1')
con = engine.connect()
db = pd.read_sql_table('datacamp', con)
print(db, '\n')

pivoted = db.pivot(index='weekday', columns='city')
pivoted1 = db.pivot(index='weekday', columns='city', values='visitors')
print(pivoted, '\n')
print(pivoted1, '\n')

# 인덱스 컬럼으로 쌓아줘
stacked = pivoted.stack(level='city')
print(stacked, '\n')

# 인덱스로 쌓은놈 다시 열로 올림
unstacked = stacked.unstack(level='city')
print(unstacked, '\n')

# 멀티 인덱스인 경우 인테스 레벨 변경
swap = stacked.swaplevel(0, 1)
print(swap, '\n')

# 소팅해서 묶어줌
sort = swap.sort_index()
print(sort, '\n')

# 두 테이블 같은지 확인
print(pivoted.equals(unstacked), '\n')

# 새로 인덱스 열 하나 추가함
reset = db.reset_index()
print(reset, '\n')

# 피봇 테이블
count = db.pivot_table(index='weekday', aggfunc='count')
print(count)

# 밑에 요약 행 보여주는 거임
sum = db.pivot_table(index='weekday', margins=True, aggfunc=sum)
print(sum)
