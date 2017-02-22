# 기반 IO인터페이스

f = open(r'C:\Users\user\Downloads\my.ini', 'r')
f1 = open(r'C:\Users\user\Downloads\DVDRentalERDiagram.pdf', 'br')

# 정수 파일 기술자 반환 - 파일에 접근할 수 있는 번호 부여하는거>??
print(f.fileno())

# f 가 터미널인 경우 true 반환
print(f.isatty())

# 읽기로 열렸는디
print(f.readable())

# 파일 포인터를 지정한 위치로 옮김 (offset 은 바이트 , whence 는 0이면 처음 1이면 현재, 2이면 끝) - 바이너리만 위치 조정가능
f1.seek(-150, 2)
print(f1.readline())

# seek 쓸 수 있는지
print(f.seekable())

# 현재 파일포인터 위치 반환
print(f1.tell())

f.flush()
f.close()
print(f.closed)


# 무가공 바이트에 대한 IO 수행 시...
import io

# 버퍼리더도 없는 완전히 저수준 바이트 읽는건데... 쓸일이 있을까...
fio= io.FileIO(r'C:\Users\user\Downloads\DVDRentalERDiagram.pdf')
print(fio.name)
print(fio.mode)
print(fio.read(100))