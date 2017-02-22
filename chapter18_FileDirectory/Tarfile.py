# tar 아카이브 파일 조작 모듈

import tarfile

f = r'C:\Users\user\Downloads\dvdrental.tar'

# 정상적으로 읽을 수 있는 tar 파일인지 확인
print(tarfile.is_tarfile(f))

# tarfile 객체 생성 모드는 '파일모드:압축방법' 형태로 입력함
# gz : gzip 압축으로,  bz2 : bzip2 압축으로
tf = tarfile.open(f, 'r:')

# 멤버명을 Tarinfo 객체 리스트로 반환
tarinfo = tf.getmembers()
print(tf.getmember('2165.dat'))
print(tarinfo)

# 멤버 이름 목록 반환
print(tf.getnames())

# 아카이브 안에서 멤버 추출해서 현재 디렉터리에 저장함
tf.extract('restore.sql', path=r'C:\Users\user\Downloads')
tf.close()

# 이거 롸이트 모드로 하면 이전에 안에 있던 파일 다 날라감...ㄷㄷ
tf = tarfile.open(f, 'a')

# 새로운 파일 넣기 - arcname 은 새로 정할 네임, recursive 는 디렉터리 안에 있는 파일 재귀적으로 더할 지 여부
addfile = r'C:\Users\user\Downloads\1991_Goldberg_FloatingPoint.pdf'
tf.add(addfile, arcname='Added PDF file', recursive=False)


tf.close()