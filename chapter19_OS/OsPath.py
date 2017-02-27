import os
from os import path

#  경로 조작을 위한 모듈
pt = r'..\Datacamp\Vincent'
pt2 = '~user\\pycharmproject'

# 상대 경로를 받아서 현재 경로를 참고해서 절대경로 반환함
ptt = path.abspath(pt)

# 기반 패스 반환
print(path.basename(pt))

# 패스의 디렉터리 반환
print(path.dirname(pt))

# 패스가 존재하는지 여부
print(path.exists(pt))

# '~user' 형태 경로를 홈 디렉터리로 대체함
print(path.expanduser(pt2))

# 환경변수 요인으로 변수 확장하는 기능 - 환경 변수 중에서 키값 $ 랑 같이 넣으면 됨
pt3 = '.\\Datacamp\\$USERDOMAIN\\some.dat'
print(path.expandvars(pt3))

# 해당 경로에대한 최근 접근 epoch 시간으로 반환
print(path.getatime(ptt))

# 생성 시간 가져옴
print(path.getctime(ptt))

# 디렉터리인지 파일인지 반환
print(path.isdir(ptt))

# 경로를 정규화함? - 윈도에서는 슬래시를 역슬래시로.. 대소문자 소문자로 통일
pt4 = '~user/Pycharmproject/'
print(path.normcase(pt4))