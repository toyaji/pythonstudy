# array 모듈은 list 랑 거의 같지만, 안에 한가지 타입만 가질 수 있어. 자바 어레이랑 비슷한듯...
import array

# 처음 생성시 변수로 타입코드를 넣어줘야함. 타입코드는 종류가 많아... c 처럼
a = array.array('b')
a.append(65)
a.append(110)

# 함수들...
print(a.typecode)
print(a.itemsize)

# 배열 저장한 메모리 위치 및 버터 길이 정보 확인
print(a.buffer_info())

# 빅엔디안 <-> 리틀엔디안 바꿔주는거임
a.byteswap()

# 몇번이나 세는거
print(a.count(65))

b = array.array('b')
b.append(45)
b.append(87)

# 끝에다가 같은 타입 객체 통으로 붙여줌
a.extend(b)
print(a)

# list 에서 가져옴
l = [10, 67, 35]
a.fromlist(l)
print(a)

# 스트링을 이진값들로 읽어서 붙여줌
s = 'paul'
a.fromstring(s)
print(a)

# 인덱스
print(a.index(45))

# a 위치 앞에 b 를 삽입
a.insert(5, 122)
print(a)

# 보여주고 제거
print(a.pop(6))

# 배열에서 처음나온 x 를 제거
a.remove(97)

# 순서뒤집기
a.reverse()

# 파일로 보내기
with open(r'C:\Users\user\Downloads\arrayout.txt', 'bw') as f:
    a.tofile(f)

# 파일서 가져오기  - f 에서 n 개 읽어와서 끝에 추가
with open(r'C:\Users\user\Downloads\arrayout.txt', 'br') as f:
    a.fromfile(f, 3)

# 리스트로만들기
li = a.tolist()
print(li)

# 문자열로 만들기
print(a.tostring())

# 유니코드 문자열로 반화  - 타입 'u' 아니면 에러!
# a.tounicode()

# 공간 효율위해 쓰는 것이라서 생성시에 리스트를 내포하면 의미가 없고, 생성기 표현식을 사용하면 좋음
b = array.array('i', (2*x for x in range(10)))
print(b)