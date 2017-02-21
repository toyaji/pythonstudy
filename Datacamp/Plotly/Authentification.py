# 먼저 온라인에서 그리는 방식 - cloud 형태로 바로 지네 사이트에서 보여주고 저장까지됨
import pandas as pd
import plotly
from plotly import graph_objs as go

# 이 부분은 온라인 인증 하는 부분
plotly.tools.set_credentials_file(username='toyaji', api_key='ytMGRN1wZKw9boTrcihj')

f = 'c:\\Users\\user\\PycharmProjects\\kospi1.csv'
df = pd.read_csv(f, sep=',', encoding='utf-8')

print(df.head())


# 뿌려줄 데이터 설정 - 요 부분이 해당 부분에서 특별한 부분 안 스면 안 뿌려짐
trace0 = go.Scatter(x=df['8260'], y=df['363'], mode='markers')
trace1 = go.Scatter(x=df['8260'], y=df['22'], mode='lines+markers')

# 리스트로 묶어주고 마지막으로 뿌려줌
data = [trace0, trace1]
plotly.plotly.plot(data, filename='first graph')


