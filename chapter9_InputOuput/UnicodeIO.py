# 유니코드 파일 여는 방법

import codecs

f = codecs.open(r'C:\Users\user\Downloads\portfolio.txt', 'r', 'utf-8', 'strict')
print(f.readline())
f.close()


# 이미 파일 객체 생성한 경우에는 wrapper 로 씌울 수 있음. 단 래퍼로 열려면 파일을 이진모드로 열어야함
f = open(r'C:\Users\user\Downloads\portfolio.txt', 'rb')
fenc = codecs.EncodedFile(f, 'utf-8')

print(fenc)
f.close()


# 유니코드 파일에다가 해당 파일이 어떤 유니코드로 작성되었는지 쓰는 경우 있음
# 이거를 BOM 문자라고 하는데 (byte-order-marker)