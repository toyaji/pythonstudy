import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# 바차트 라벨용 리스트
cd = ['stock', 'finance']


[stock, finance] = [21, 7]    # 요거는 트위터에서 원래 긁어오는 건데 다른 파일에 있어서 그냥 임의로 데이터 만듬

# seaborn 바차트 그리는 함수에서 첫번째 인자값은 x축 라벨, 두번째 인자값이 바차트 그릴 데이터 리스트
ax = sns.barplot(cd, [stock, finance])
ax.set(ylabel="count")
plt.show()