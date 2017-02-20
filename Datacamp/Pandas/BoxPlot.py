import pandas_datareader as pdr
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime


start = datetime(2017, 1, 1)
end = datetime(2017, 2, 11)
stock = pdr.DataReader("078930.KS", "yahoo", start, end)

df = pd.DataFrame(stock)
print(df)

# 박스 플롯 보는법
print('http://newmkka.tistory.com/348')

# 현재 데이터 에서 끌어올 칼럼 설정
gap = ['High', 'Low']
df[gap].plot(kind='box', subplots=True)

plt.show()