import pandas as pd
from os.path import expanduser
from plotly import graph_objs as go
from plotly import plotly, offline

file = expanduser(r'~\downloads\농촌마을별+인원정보_20170411.csv')
df = pd.read_csv(file, encoding='euc-kr')

# 마스킹 만들기
manmask = df.columns.str.contains('남자')
womanmask = df.columns.str.contains('여자')
# mask = manmask | womanmask

man = df[df.columns[manmask]]
man = man.stack().unstack(level=0)
man = man.sum(axis=1)

woman = df[df.columns[womanmask]]
woman = woman.stack().unstack(level=0)
woman = woman.sum(axis=1)

index = man.index.str.split()
dex = []
for i in index: dex.append(i[1])


print(man)
print(woman)
print(dex)

man.to_csv(expanduser(r'~\documents\man.csv'), index=dex)
woman.to_csv(expanduser(r'~\documents\woman.csv'), index=dex)

trace1 = go.Bar(x=dex, y=man, name='남성', marker=dict(
        color=['#9BABA8', '#9BABA8', '#9BABA8', '#9BABA8', '#C96B00', '#9BABA8', '#9BABA8', '#9BABA8']
        ))
trace2 = go.Bar(x=dex, y=woman, name='여성', marker=dict(
        color=['#E7EADF', '#E7EADF', '#E7EADF', '#E7EADF', '#E0B300','#E7EADF','#E7EADF','#E7EADF']
        ))

data = [trace1, trace2]

layout = go.Layout(barmode='stack')
fig = go.Figure(data=data, layout=layout)
offline.plot(fig, filename='RuralCensus.html')