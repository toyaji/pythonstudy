path = 'C:\\Users\\user\\Downloads\\'

f = open(path + 'portfolio.txt', 'a')        # r, w, a 가 있음 a 는 추가모드

f.write('New line added!')

f.close()

# f2 = open(path + '','br')    # 이진파일 여는 옵션

# f2 = open(path + '','U')     # \n, \r, \r\n 처럼 줄바꾼 문자 플랫폼마다 다른데 이걸 다 통일해줌 플랫폼 상관없이 파일 읽을수 있음

# f2 = open(path + '','r+')    # 추가작업 가능 입출력 모두 가능함


f2 = open(path + 'IO.txt', 'r+', buffering=1, encoding='UTF-8', newline='\n')

# newline 옵션으로 줄바꿈 문자 특정할 수 있음
# r+ 옵션은 덮어써버림 (읽기 + 쓰기), w+ 는 일단 여는 순간 길이 0으로 기존거 없애고 이것만 적음, a+ 는 뒤에다가 붙이고...


for i in range(10):
    f2.write(str(i) * 100 + '\n')
# 덮어쓴 부분 은 현재 버퍼에 있기 때문에 다시 출력이 되지 않고 그 뒤에 부분부터 출력이 나오네...

print(f2.read(20))      # 최대 [n] 바이트까지 읽어옴
print(f2.readline(30))  # 최대 n개의 문자까지 읽어옴
print(f2.readlines())


f2.close()




f3 = open(path + 'binaryInput.txt', 'bw')        # r, w, a 가 있음 a 는 추가모드

for i in range(10):
    f3.write((bytes(str(i)*100 + '\n', encoding='UTF-8')))

f3.close()




f4 = open(path + 'binaryInput.txt', 'br')        # r, w, a 가 있음 a 는 추가모드

while True:
    line = f4.readline()
    print(line)
    if not line:
        break

f4.close()