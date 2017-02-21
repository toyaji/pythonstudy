import pandas as pd
import plotly
from plotly import graph_objs as go

data = go.Scatter(x=['a', 'b', 'c', 'd'], y=[5, 7, 19, 3])

layout = go.Layout(title='This is offline Bar')

f = 'c:\\Users\\user\\PycharmProjects\\kospi1.csv'
df = pd.read_csv(f, sep=',', encoding='utf-8')

print(df.head())

# 뿌려줄 데이터 설정 - 요 부분이 해당 부분에서 특별한 부분 안 스면 안 뿌려짐
trace0 = go.Scatter(x=df['8260'], y=df['363'], mode='markers')
trace1 = go.Scatter(x=df['8260'], y=df['22'], mode='lines+markers')

# 리스트로 묶어주고 마지막으로 뿌려줌
data = [trace0, trace1]

# 요 부분인데, html 파일로 만들고 현재 경로에 저장하고 파일 여는것 까지 함.
plotly.offline.plot(data, filename='First item.html')