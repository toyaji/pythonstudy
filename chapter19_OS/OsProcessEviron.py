import os

# 현재 작업 디렉터리를 주어진 패스 경로로 전환
# print(os.chdir())

# 현재 작업 디렉터리 반환
print(os.getcwd())

# 현재 프로세스의 실제 프로스세 id 반환  - pid 개념은 유닉스에서 쓰는듯...
print(os.getpid())

# 환경변수 설정 - 이름, 벨류
os.putenv('paul', '1234')

