import sys

print(sys.path)


#  sys.path 에 나열된 순서대로 모듈을 검색해서 로드함
#  이때, sys.path 에 추가로 경로를 더해주거나, .zip 이나 .egg 를 넣어서 안에 있는 파일 임포트할 수 있음

sys.path.append("C:\\Users\\user\\PycharmProjects\\pythonstudy\\ImportTest.zip")

print(sys.path)

import ImportFromZip