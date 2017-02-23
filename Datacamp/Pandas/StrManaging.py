import pandas as pd

# 문자셋을 추정해주는 모듈임 - 몹시 굿!!
import chardet

file = r'C:\Users\user\PycharmProjects\kospi.csv'

# 현재 판다스가 uft8 을 못 읽어서 chardet 으로 한번 더 처리함
with open(file, 'rb') as f:
    result = chardet.detect(f.read())

# 헤더 라인이 없어서 한번 더 데이터 프레임으로 넣어주면서 헤러칼럼 정보 입력함 - name 셋팅해주기
header = ['num', 'code', 'kind', 'name', 'price', 'unknown', 'volume', 'period']
df = pd.read_csv(file, sep=',', encoding=result['encoding'], names=header)

print(df.head())


# 공백문자 쓸어내기
df['name'] = df['name'].str.strip()
print(df.head())

# 특정 문자 포함 확인 - 정규표현식 사용 가능
samsung = df['name'].str.contains('[삼성]')


#

