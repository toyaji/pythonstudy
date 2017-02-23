import pandas as pd
from matplotlib import pyplot as plt

f = r'C:\Users\user\PycharmProjects\yahoo.csv'
df = pd.read_csv(f, index_col='Date', parse_dates=True)

# 리샘플링 하고 기간 구분자 안에 주면 해당 기준으로 다시 필터링함 ('6h', 'd' 요런식으로...)
df1 = df['Open'].resample('M').count()
print(df1.head())

# 두단계 필터
df2 = df['Close']['2012-Jun']
print(df2.mean())
print(df2.max())

# 롤링이라고 해서 튀는값 상쇄하도록 보는 방법
df3 = df['High'].rolling(window=15).mean()
print(df3)
df3.plot()
plt.show()

# 추출 뽑아서 다시 데이터프래임 만드는법
df4 = pd.DataFrame({'Unsmoothed':df['High'], 'Smoothed':df3})
print(df4.head())