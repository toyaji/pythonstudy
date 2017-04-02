from os import environ, path, getenv
import pandas as pd

# 현재 유저홈 디렉토리 가져오는 다양한 방법
home = environ['HOMEPATH']
print(home)
print(getenv('HOMEPATH'))

# 요 방법이 가장 확실하게 어떤 OS 에서나 크로스 플랫폼하게 사용가능한 형태임
allhome = path.expanduser('~')
print(allhome)

file = allhome + '\\PycharmProjects\\kospi.xlsx'

# 헤어 없는 경우에 가져오는 헤더 논 조건으로 가져와서 헤더 입히기
df = pd.read_excel(file, sheetname=0, header=None)
print(df.head())
df.columns = [x*2 for x in range(1,9)]
print(df.head())

# 칼럼 불필요한 컬럼 통째로 떨구기
df_dropped = df.drop([6,12], axis='columns')
print(df_dropped.head())