import requests
import pandas as pd
import re
from matplotlib import pyplot as plt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
r = requests.get(url)
html = r.text

raw_data = html.splitlines()
new = []

# 공백 잘라서 리스트로 만드는 작엄 - 정규표현식 사용하면 훨씬 간결하구나...
for line in raw_data:
    new.append(re.split('\W{2,10}', line))

# 조금더 정밀하게 잡고, 아이템 별로 float 로 변경하는 중... 에러뜨는 애들 있어서 한번에 되지를 않네...ㅠㅠ
for line in new:
    line[8] = re.sub('\"', '', line[8])
    if len(line) > 9:
        line[8] += line[9]
    for i in range(6):
        try:
            line[i] = float(line[i])
        except:
            pass

df = pd.DataFrame(new)

print(df.dtypes)

df.plot(kind='scatter', x=0, y=2)

plt.show()