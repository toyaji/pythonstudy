from sqlalchemy import Table, MetaData, create_engine, insert, select

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/db1')

meta = MetaData()

with engine.connect() as con:
    data = Table('data', meta, autoload=True, autoload_with=engine)

    # 신규 데이터 집어넣는 방법
    stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)
    results = con.execute(stmt)
    print(results.rowcount)

    # 특정 칼럼에 명령 맞는애 불러 오는 방법임
    stmt2 = select([data]).where(data.columns.name == 'Anna')
    print(stmt2)
    print(con.execute(stmt2).first())

    # 데이터 여러건 넣는 방법
    values_list = [
        {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
        {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
    ]
    stmt3 = insert(data)
    print(stmt3)
    print(con.execute(stmt3, values_list).rowcount)