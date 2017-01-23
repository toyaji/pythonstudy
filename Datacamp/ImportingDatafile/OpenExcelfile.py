import pandas as pd

# 이렇게 읽어오면 'xl' 은 <class 'pandas.core.frame.DataFrame'> 로 저장됨.

file = r'c:\Users\user\Downloads\시간계획표.xlsx'
xl = pd.read_excel(file)  # 판다스를 먼저 임포트해야함

print(type(file))
print(type(xl))


# 다음의 경우,

newfile = pd.ExcelFile(file)  # 요렇게 해야 io 의 parse 함수 써서 시트명 가져오거나 할 수 있음

xl1 = newfile.parse('상반기계획')
xl2 = newfile.parse(0)

print(type(newfile))
print(xl1.head())
print(xl2.head())