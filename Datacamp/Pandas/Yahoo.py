import pandas_datareader as pdr
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime
from matplotlib import pyplot as plt

# from ya

start = datetime(2010, 1, 1)
end = datetime(2017, 2, 14)
stock = pdr.DataReader("078930.KS", "yahoo", start, end)

print(stock.info())
print(stock.head())

df = DataFrame(stock)
plt.plot(df)
plt.show()
df.plot(subplots=True)    # 여러개 하위 그래프로 보여줌

close_series = df['Close']
# plt.plot(close_series)
close_series.plot()     # 위에나 똑같음
plt.show()

gap = ['High', 'Low']
df[gap].plot()
plt.yscale('log')
plt.ylabel('Price')
plt.xlabel('Period')
plt.show()

df['Open'].plot(color='b', style='.-', legend=True)     # 색깔하고 점 연결하는 방법 넣어주고, 레전드는 선 설명붙는 박스임
df['Close'].plot(color='y', style='.', legend=True)

plt.axis(('2013', '2014', 40000, 80000))                # 양축에서 어느 부분만 뽑아서 보여줄지
plt.show()