import bz2

# bz2 압축 파일을 열거나 써서 일단 file 객체처럼 쓸 수 있게 만들어줌
with bz2.BZ2File(r"C:\Users\user\Downloads\bz2.bz2", 'a') as f:
    for i in range(10000):
        f.write(bytes(i))

# 테이블 블록 압출 할 수 있는 압축객체 생성 - 인자로 1 ~ 9 까지 압축정도 넣어야함
comp = bz2.BZ2Compressor(9)

# 압축객체에 바이트 문자열 데이터 추가
comb = open(r'C:\Users\user\Downloads\AtomSetup-x64.exe', 'br')

with bz2.BZ2File(r"C:\Users\user\Downloads\atom.bz2", 'a') as f:
    for line in comb:
        f.write(comp.compress(line))