import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

f = r'C:\Users\user\PycharmProjects\yahoo.csv'
df = pd.read_csv(f, parse_dates=['Date'])

# 아래 방식으로 하면 데이트 인덱싱이 가능함
df1 = pd.read_csv(f, index_col='Date', parse_dates=True)

print(df.info())
print(df1.info())
print(df1.index)

# 타임포맷 세팅
time_format = '%Y-%m-%d %I:%M %P'
dtime = pd.to_datetime(df['Date'], format=time_format)

# 타임시리즈 생성하기
time_series = pd.Series(df['Open'], index=dtime)
print(time_series.head())

# 타임 셋 판다스가 알아서 확인함  ?? 에러나는 이유 몰까...
print(df1.loc['2010-Oct'])

# 리인덱싱 하는법
red = df.reindex(df1.index)