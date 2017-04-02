import pandas as pd
from matplotlib import pyplot as plt

f = r'C:\Users\Paul\Documents\GitHub\seaborn\seaborn-data\tips.csv'
df = pd.read_csv(f)

# 줄 나눠서 나오도록 설정하는 것임 (총 몇개 그릴 건지 인자값으로 넘겨줄 수 있음)
fig, axes = plt.subplots(nrows=2, ncols=1)

# Probability density function (확률밀도함수) 그리기 - ax 아마도 몇번째 서브플랏에다 그릴지,, 종류는 그래프 종류,,, 놈드는 확률값으로 보여주는거임
# bins x축을 몇 분율로 잘라서 보여줄지 인듯함... range 는 x  값 표시할 레인지
df['tip'].plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0, 10))

# cumulative density function (누적 분포함수) 그리기 - cumulative 만 셋팅해주면 됨
df['tip'].plot(ax=axes[1], kind='hist', normed=True, cumulative=True, bins=100, range=(0, 8))

plt.show()
plt.close()

import cv2

from cv2