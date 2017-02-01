from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine(r'sqlite:///C:\Users\user\Downloads\Chinook_Sqlite.sqlite')

meta = MetaData()

with engine.connect() as con:
    empl = Table('Employee', meta, autoload=True, autoload_with=engine)
    stmt = select([empl])       # 셀렉트 함수 쓸려면 리스트로 인자값 넣어줘야함
    data = con.execute(stmt).fetchall()

    first_row = data[0]        # 셀렉트로 뽑아낸 ResultProxy 객체를 인덱싱으로 줄을 걸러낼 수 있음

    print(first_row, '\n')
    print(first_row['City'])   # 다시 걸래낸 줄은 튜플로 나오니가 여기서 필요한 칼럼 명으로 데이터 쿼리 가능함