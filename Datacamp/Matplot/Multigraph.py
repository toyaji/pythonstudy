import pandas as pd
import matplotlib.pyplot as plt
import chardet

file = r'C:\Users\user\Downloads\DataDownload\새만금유역_수위계측정보_2016\새만금유역 수위계측정보_가력도_2016.csv'

# uft8 판다스가 못읽어서 코덱 찾아오기
with open(file, 'rb') as f:
    result = chardet.detect(f.read())

df = pd.read_csv(file, encoding=result['encoding'], skipfooter=4, engine='python')
print(df.head())

"""
df = df.stack()
df = df.unstack(level=0)
df.columns = df.iloc[0]
print(df.head())

"""
plt.subplot(3, 1, 1)
plt.plot(df['2016-01-01'], 'red', label='1월1일')
plt.subplot(3, 1, 2)
plt.plot(df['2016-01-03'], 'blue', label='1월3일')
plt.subplot(3, 1, 3)
plt.plot(df['2016-01-05'], 'yellow', label='1월5일')
plt.xlabel('Sea_level')

# 레전드라고 해서 표시 해주는 부분 만들기
plt.legend(loc='center')

plt.tight_layout()
plt.show()

