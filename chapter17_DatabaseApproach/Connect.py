# 파이썬은 관계형 데이터베이스 다루는데 크게 두 객체 있음.
# 그중 먼저가 'Connect' 인데, 데이터랑 연결하는거임
import psycopg2 as pg
import sqlalchemy as sq

# 데이터 베이스 연결 - 예시는 postgresql : 일단 이게 기본임. (dns= '호스트네임:데이터네임')
c = pg.connect(host='localhost', database='dvdrental', port=5433, user='postgres', password='1234')
c.close()



# 이거는 사이코피지 튜토리얼에 나오는 관련 정보 저장 방법 - 좀 더 복잡하게
from configparser import ConfigParser

file = r'C:\Users\user\PycharmProjects\database.ini'
def config(filename=file, section='postgresql'):
    # 파서 만들어서 읽기
    parser = ConfigParser()
    parser.read(filename)

    # 섹션 얻어서 디폴트로 하기
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in thr {1} file'.format(section, filename))

    return db


def connect():
    conn = None
    try:
        # 커넥션에 필요한 변수들 읽어오기
        params = config()
        print('Connecting to the PostgreSQL database ...')
        conn = pg.connect(**params)

        # 커서 만들기
        cur = conn.cursor()

        # 쿼리
        print('PostgreSQL database Version :')
        cur.execute('SELECT version()')

        # 가져온거 보여주기
        db_version = cur.fetchone()
        print(db_version)

        cur.close()

    except (Exception, pg.DatabaseError) as er:
        print(er)

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")


if __name__ == '__main__':
    config()
    connect()

# 써보니까. 연결은 sqlalchemy 로 하는게 가장 쉽고,
# 엔진 생성하면쿼리도 직접 입력하면 지가 인식하니까 좋은 듯