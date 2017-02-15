import pandas as pd
from zipfile import ZipFile

# zip 파일 열려면 zipfile 모듈 필요함
with ZipFile(r'C:\Users\Paul\Downloads\WDI_CSV.zip') as myzip:
    print(myzip.filelist)
    with myzip.open('WDI_Data.csv') as file:
        # 판다 읽기로 청크 단위로 끊어서 가져올 수 있음
        data = pd.read_csv(file, chunksize=300)
        onechunk = next(data)
        print(onechunk.head())

# 특정 조건 맞는 거만 다시 저장하기
unnon = onechunk[onechunk['2010'] > 10]
print(unnon.head())


# 새로 컬럼 만들기
print()
unnon['New Column'] = [len(row) for row in unnon]
print(unnon.head())