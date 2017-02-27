import os

# 현재 환경 변수 매핑 객체 반환
print(os.environ)

# 현재 os 의 줄바꾼 문자열 반환
print(bytes(os.linesep, encoding='ASCII'))

# 임포트할 os 종속 모듈
print(os.name)

# 경로 연산에 사용하는 os 표준 모듈
os.path
