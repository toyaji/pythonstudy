import io

f = open(r'C:\Users\user\Downloads\DVDRentalERDiagram.pdf', 'rb')
f1 = open(r'C:\Users\user\Downloads\indicator life_expectancy_at_birth.xlsx', 'rb+')

# 버퍼 사이즈 설정해 줄 수 있음
bf = io.BufferedReader(f, 100)

# 해당 버퍼 안에서 만큼 읽기 - 읽은만큼 버퍼 비워짐
print(bf.read(10))

# 현재포인터 위치에서 최대 n 바이트 데이터 반환  -  버퍼 비워지지 않으면서 토해내는게 맞는듯...
print(bf.peek(2))

# 주어진 데이터만큼 읽고 모자라면 파일에 read 한번 수행함  .. 이거 이해아나네...
print(bf.read1(112))

# 임의 접근 가능한 io 스트림에 읽기 쓰기 수행함 - 읽기 쓰기 둘다 되야함
bfr = io.BufferedRandom(f1, 100)
print(bfr.read(10))