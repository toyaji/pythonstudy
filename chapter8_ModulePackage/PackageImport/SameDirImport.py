from . import ImportEx2

ImportEx2.Too()

# 임포트 할때 현재 디렉토리 의미하는게 바로 . 임
# 현재 위에 코드 에러 나는데 관련해서 스택플로우 설명 있음 : http://stackoverflow.com/questions/16981921/relative-imports-in-python-3

from ..ImportEx import foo

foo()

# 그 상위 디렉토리에서 파일 찾는 방법이 .. 임

# 임포트 할때 접근 경로 변경하려면 __init__ 파일 안에 패키지 생성시 형성되는 __path__ 를 커스터마이징 하면 가능함