from bokeh.plotting import figure, show, output_file, ColumnDataSource
import pandas as pd
from os.path import expanduser as ex

file = ex(r'~\Downloads\table.csv')
df = pd.read_csv(file)
source = ColumnDataSource(df)   # 보케 기본 객체인 컬럼데이터소스로 전환해주고 사용하는 방법임

p = figure(x_axis_type='linear', x_axis_label='Time', y_axis_label='Price')

# 이게 ColumnDataSource 로 변형이 안되서 표에서 아무 값도 안뜨는듯함.... circlr 은 되는데.. line 은 판다스 프레임이 바로 안먹힌다...?
p.line('Date', 'Adj Close', source=source)

output_file('Bit_Price.html')
show(p)


