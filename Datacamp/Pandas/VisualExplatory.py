import pandas_datareader as pdr
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime


start = datetime(2010, 1, 1)
end = datetime(2017, 2, 11)
stock = pdr.DataReader("078930.KS", "yahoo", start, end)

df = pd.DataFrame(stock)

# 현재 데이터 에서 끌어올 칼럼 설정
gap = ['High', 'Low']
df.plot(y=gap)

# 그래프 전체에 이름 주기
plt.title('Monthly stock prices')

# 라벨 주기
plt.ylabel("Price ($US)")

plt.show()