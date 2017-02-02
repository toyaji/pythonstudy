path = 'C:\\Users\\user\\Downloads\\'

f = open(path + 'IO.txt', 'r+', buffering=1, encoding='UTF-8', newline='\n')

# seek 메서드에 두개 인자가 있음. 이중 whence 가 0 이면 시작위치서 offset, 1 이면 현재 위치서 offset, 2 이면 파일끝에서부터
# offset 만큼 바이트 이동함
f.seek(300, 0)
print(f.readline())

# 아래처럼 현재 위치나 후방위치에서 움직이는 옵션은 바이너리만 가능함
"""
f.seek(100, 1)
print(f.readline())
f.seek(-200, 2)
print(f.readline())
"""

print(f.mode)
print(f.name)
print(f.encoding)

f.close()