import os

# 현재 환경변수 접근할 수 있도록 해주는 모듈

path = os.environ["PATH"]
user = os.environ["USERNAME"]
encoding = os.environ["PYTHONIOENCODING"]

print(path, user, encoding)


# 환경변수에 직접 아이템 넣을 수도 있음. 변경주게되면 현재 실행중인 프로그램하고 하위 프로세스 영향

os.environ['FOO'] = "bar"

print('\n', os.environ)