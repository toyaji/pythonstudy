import pandas as pd
import os.path
import sqlite3
import numpy as np


# sqlite 엔진 연결 해서 테이블 명 가져오기
file = '~user\\Downloads\\Chinook_Sqlite.sqlite'
path = os.path.expanduser(file)
con = sqlite3.connect(path)
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# 판다스 데이터 프레임으로 테이블끌어오기
result = pd.read_sql("SELECT * FROM Customer;", con)
print(result.head())

# 일반 인덱싱과 loc, iloc
print()
print(result['Fax'][4])   # 일반 인덱싱의 경우엔 칼럼이 먼저고, 열이 다음임
print(result.loc[4, 'Fax'])   # loc 의 경우는 로우가 먼저고 다음이 열
print(result.iloc[4, 9])      # iloc 는 숫자 인덱싱


# 특정 부분 끌어오기
print()
print(result.loc[4:10, :'Company'], '\n')
print(result.loc[[5, 12, 23], ['Country', 'Phone']], '\n')

# 시리즈와 데이터프레임 - 시리즈는 데이터 프레임 구성하는 단일 열을 의미함
# 시리즈의 경우는 조건주는 마스크나 불린, 타임 시리즈 등으로만 사용됨 ? 그 자체로 인덱싱이나 프린팅이 안됨
print(type(result['Email']))
print(type(result[['Email']]), '\n')


# 필터링 - &, | 요런 연산자 사용가능함
mask = result['Company'].isnull() & result['Fax'].isnull()
print(result[mask].head(), '\n')

# 조건 해당하는 줄에 대해서 새로 nan 생성하기
result['SupportRepId'][mask] = np.nan

# nonzero 가 하나도 있는지 없는지
print(result.loc[5:7, result.notnull().all()], '\n')

# 데이터프레임 카피하기
df2 = result.copy()

# Nan 있는 칼럼 떨구기
df2.dropna(how='any')   # any 인 경우에 하나만 nan 이여도 열 떨구기, all 인 경우 모든 값이 nan 이여야 떨굼
# df2.dropna(thresh=3)  # 요런식으로 적어도 몇개 이상이 nan 이 아니어야 살려줌...
print(df2.shape)
