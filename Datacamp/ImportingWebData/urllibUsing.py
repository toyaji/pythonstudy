from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://chart.finance.yahoo.com/table.csv?s=YHOO&a=11&b=24&c=2016&d=0&e=24&f=2017&g=d&ignore=.csv'

data = urlretrieve(url, r'c:\Users\user\Downloads\yahooPrice.csv')

df = pd.read_csv(url, '\b', ',')   # seperator 2개 설정해서 현재 야후 주가 csv 로 가져온 거임
print(df.head())
print(df.keys())

pd.DataFrame.hist(df)  # 히스토그램으로 보여줌
plt.xlabel('')
plt.ylabel('count')
plt.show()

# 가져오는 파일이 엑셀인 경우
"""
xl = pd.read_excel(url, sheetname=None)
print(xl['1700'].head())
# 시트명을 인덱스로 집어넣어줘야함

"""