from sqlalchemy import *

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')
engine2 = create_engine('mysql+pymysql://paul:happygk2@localhost:3306/db1')
# 먼저 pymysql 방언이 깔려있어야함

print(engine.table_names())
print(engine2.table_names(), '\n')

meta = MetaData()

with engine.connect() as con:
    census = Table('census', meta, autoload=True, autoload_with=engine)

    stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop')])   # 요런식으로 범위 줄 수도 있음
    stmt = stmt.group_by(census.columns.state).order_by(desc('pop'))

    female2000 = func.sum(case([(census.columns.sex == 'F', census.columns.pop2000)], else_=0))
    # case 문을 통해서 조건에 맞는 녀석들 가져오는 형태임. 이거 괄호 안은 형태가 좀 복잡함... ㅜㅜ
    total2000 = cast(func.sum(census.columns.pop2000), Float)
    # 자바에 캐스팅 값은 거임. 일단 플로트로 만들어서 가져옴
    # 단, 현재 mysql 에서는 float 타입 지원안해줘서 무시하고 지나감

    stmt1 = select([female2000 / total2000 * 100])

    print(stmt)
    print(stmt1, '\n')


    results = con.execute(stmt).fetchall()
    percentage = con.execute(stmt1).scalar()

    print(type(percentage), '\n')




for result in results:
    print('{}-{}'.format(result.state, result.pop))

print(percentage)