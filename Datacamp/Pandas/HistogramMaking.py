import pandas as pd
import matplotlib.pyplot as plt

file = r'C:\Users\Paul\PycharmProjects\kospi.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

df = xl.parse('kospi', skiprows=[1], names=['코드', '종목명', '현재가', 'PER', 'EPS', '최근결산일'])

# 시트명으로 시트 하나 찝어서 판다스 데이터 프레임으로 변경하기
# 'name=' 쓸려면 현재 컬럼 숫자만큼 이름 넣어줘야함

plt.hist(df['현재가'])
plt.show()