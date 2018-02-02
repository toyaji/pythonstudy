import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

total = pd.read_excel(r'C:\Users\toyaji\Documents\수업\국제개발\데이터\meat_consumption(통계수업).xlsx', 'Total')
sns.set(font_scale=1.7, )

total = total[total['Year']<2017]
year = reversed(total.Year.unique())
pallete = sns.cubehelix_palette(27)

f, ax = plt.subplots(figsize=(20, 10))
plt.ylim(0, 0.10)
plt.xlim(-15, 60)
for y, p in zip(year, pallete):
    tf = total[total['Year'] == y]['sheep']
    g = sns.distplot(tf, label=str(y), ax=ax, hist=False, color=p)
    ax.axvline(tf.mean(), color=p, ymax=0.1)

plt.legend(ncol=2)

plt.title("Sheep Distribution (1990-2016)")
plt.savefig("Sheep Distribution.jpg")
plt.show()
