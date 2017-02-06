from sqlalchemy import *

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

meta = MetaData()

with engine.connect() as con:
    census = Table('census', meta, autoload=True, autoload_with=engine)
    state_fact = Table('state_fact', meta, autoload=True, autoload_with=engine)

    stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])     # 둘이 관계 relationship 정의되 있는 경우에 이렇게 다른 테이블에서 잘라올 수 있음
    stmt1 = select([census.columns.state, func.sum(census.columns.pop2000), state_fact.columns.census_division_name])                                        # 두 테이블 전체 칼럼 선택
    stmt2 = stmt1.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
    # 두 테이블 같이 합쳐서 뽑아내는데, 합치는 방법은 join() 함수의 두번째 인자값으로 줘야함

    stmt2 = stmt2.group_by(state_fact.columns.census_division_name)



    print(stmt)
    print(stmt1)
    print(stmt2)

    results = con.execute(stmt2).fetchall()

for result in results:
    print(result)