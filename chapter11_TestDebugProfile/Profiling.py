# 명령줄에서 python -m cProfile someprogram.py 로 볼 수 있음

from Datacamp.RDBMS import SQLAlchemyTable
import profile


profile.run('SQLAlchemyQuery')
# 프로파일 함수를 이용한 프로파일러 실행 결과