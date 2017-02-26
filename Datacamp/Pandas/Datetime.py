import pandas as pd
from matplotlib import pyplot

f = r'C:\Users\user\PycharmProjects\yahoo.csv'
df = pd.read_csv(f)
df1 = pd.read_csv(f, index_col='Date', parse_dates=True)

# 타임객체 concact 해서 새로 만들수 있음
timezone = pd.to_datetime(df['Date'] + ' 00:00:00')

# timezone 변경
timezone_seoul = timezone.dt.tz_localize('Asia/Seoul')
print(timezone_seoul.head())
timezone_beijing = timezone.dt.tz_localize('Asia/Shanghai')
print(timezone_beijing.head())

# 마스크 설정 - 불린값 주는 걸로 조건 미리 셋팅해놓고 집어넣어서 리샘플 가능함
mask = df['Open'] > 40000
print(df[mask].head())

# 타임 객체 끌어다가 인덱스 셋팅 하는법
df.Date = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)
print(df.head())

# 구간 나눠서 플랏 그리기 - 선그리는 타입 잇음 확인하면 좋아...
df.Open['2013-Dec':'2014-Mar'].plot(title='Yahoo Price', style='c+-')
pyplot.show()