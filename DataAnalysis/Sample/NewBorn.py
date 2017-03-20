from os import path
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path = path.expanduser(r"~\Downloads\DataDownload\pydata-book-master\ch02\names\yob2010.txt")
names2010 = pd.read_csv(path, names=['name', 'sex', 'birth'])

# 성별 총계
print(names2010.groupby('sex').birth.sum())

# 전체 연도 데이터 하나로 만들기
years = range(1880, 2011)

piece = []
columns = ['name', 'sex', 'births']

for y in years:
    path = r"~\Downloads\DataDownload\pydata-book-master\ch02\names\yob%d.txt" % y
    frame = pd.read_csv(path, names=columns)

    frame['year'] = y
    piece.append(frame)

# 하나의 df 로 만들기 - concat 함수 쓰면 쉽게 합칠 수 있음
names = pd.concat(piece, ignore_index=True)
print(names.info())

# 연도나, 성별로 피벗하기
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births.tail(), '\n')

# 각 이름이 출생율에서 차지하는 비율 확인하기
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)
print(names.head(), '\n')

# 해당 비율의 총합이 1이 되는지 Sanity test 실시하기
print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1), '\n')

# 연도별 성별에 따른 빈도수 높은 이름 1000개 추출
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

print(top1000)

# 상위 천개에서 남녀 구분하기
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

# 전체 출생 수 피벗 테이블로 만들기
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
print(total_births.info())

# 이름 추이 그래프로 그려보기
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
plt.show()

# 다양한 이름 사용하는 경향 확인하기
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex',
           yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
plt.show()

# 남아중에서 50% 까지 얼마나 많은 이름 나오나 확인해보기
df = boys[boys.year == 2010]
prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()     # cumsum() 은 넘파이 메서드 .. cumulative sum 임
print(prop_cumsum[:10], '\n')

print(prop_cumsum.values.searchsorted(0.5), '\n')   # searchsorted 하면 특정값 되는 위치 반환해줌

df = boys[boys.year == 1900]
in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
print(in1900.searchsorted(0.5) + 1, '\n')

# 연도별로 50% 뽑아내는 함수 만들기
def get_qunatile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_qunatile_count)
diversity = diversity.unstack('sex')

diversity.head()
diversity.plot(title='Number of popular names in top 50%')
plt.show()


# 이름의 마지막 열의 변화 확인
get_last_letter = lambda x: x[-1]
last_letter = names.name.map(get_last_letter)           # 결과값이랑 공통항목 찾아서 매핑해줌
last_letter.name = 'last_letter'
table = names.pivot_table('births', index=last_letter, columns=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
print(subtable.head())

# 이렇게 구한 이름을 연도별로 막대그래프로 표현하기
letter_prop = subtable / subtable.sum().astype(float)
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
plt.show()