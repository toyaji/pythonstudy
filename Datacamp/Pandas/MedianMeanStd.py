import pandas as pd
from matplotlib import pyplot as plt

f = r'C:\Users\user\Downloads\indicator life_expectancy_at_birth.xlsx'
df = pd.read_excel(f, sheetname='Data', na_values=0)

# NaN 값 0으로 채우기
print(list(df))
# df = df.fillna(0)
print(df.head())

# 눌 값 있는 지 확인
print(df[2016].isnull())

# 최대, 최소, 중앙값, 평균, 표준편차
print(df[1801].max())
print(df[1801].min())
print(df[1801].mean())
print(df[1801].median())
print(df[1801].std())

# 일반적인 값 묘사 - 눌 값 잇으면 에러남 % 를 못구해
print(df[1987].describe())
df[1987].plot(kind='box')
plt.show()

# 민값 연결해서 그래프 그리기
mean = df.mean(axis='columns')
mean.plot()
plt.show()


# 5% 95% 등으로 값 가져오기 리스트로 넣어줘야함!!!! - 역시나 눌값 있으면 에러나 퍼센티지를 못구함
df[2000] = df[2000].fillna(0)
print(df[2000].quantile([0.05, 0.95]))

# 박스 차트 여러개로 띄우기
years = [1800, 1850, 1900, 1950, 2000]
df[years].plot(kind='box')
plt.show()
