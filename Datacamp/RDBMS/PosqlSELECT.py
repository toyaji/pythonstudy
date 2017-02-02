from sqlalchemy import create_engine, select, Table, MetaData

# 현재 데이터는 데이터캠프 서버에서 가져오는거임
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

meta = MetaData()

# 현재 서버에서 퍼비션 부정된듯함
with engine.connect() as con:
    census = Table('census', meta, autoload=True, autoload_with=engine)
    stmt = select([census]).where(census.columns.state == 'New York')           # 해당 열이 일치하는 경우 가져오는 명령
    results = con.execute(stmt).fetchall()

    stmt2 = stmt.where(census.columns.state.in_(states))                        # in_() 인자값 안에 주어진 칼럼의 전체 가져오는 방법
    for result in con.execute(stmt2):
        print(result.state, result.pop2000)

for result in results:
    print(result.age, result.sex, result.pop2008)