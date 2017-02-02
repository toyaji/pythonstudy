from sqlalchemy import create_engine

# PostSQL 파이썬에서 쓸려면 먼저 psycopg2 라는 라이브러리 설치해야함. 이게 postSQL의 파이썬 버전 방언(dialect)임
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# 현재 데이터캠프 서버에 접속해서 가져오는 형태임
"""
postgresql+psycopg2://        방언 및 드라이버 명시
student:datacamp              username 하고 패스워드
@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432            호스트 : 포트
/census                       데이터베이스명

"""
print(engine.table_names())


# 요 밑에는 온라인에서 찾은 로컬호스트에다가 Postgresql 데이터베이스 만드는 방법
# 로컬에서 쓸려면 일단 Postgresql 설치해야 되고 그 다음에 서버 연결해야함
# 오픈소스다 보니 제공하는 곳 두군데고 조금 다른듯(?)

import psycopg2 as pg2

# conn = pg2.connect(database="postgres", user="paul", password="1234", host="127.0.0.1", port="5432")
# conn = pg2.connect("host = localhost dbname=postgres user=paul password=1234 port=5432")
# 같은 결과
# jdbc:postgresql://localhost:5432/postgres