from sqlalchemy import create_engine, MetaData, Table, Column, INTEGER, String, Float, select, update
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:happygk2@localhost:5432/postgres')

meta = MetaData()

with engine.connect() as conn:

    empl = Table('employee', meta, autoload=True, autoload_with=engine)
    own = Table('owner', meta, autoload=True, autoload_with=engine)

    stmt = update(empl).values(wage=100000)
    print(stmt)

    stmt = stmt.where(empl.columns.name == '신바울')
    print(stmt)

    results = conn.execute(stmt)

    # 다른 테이블 하고 연관관계 엮어서 저장하기
    stmt1 = select([own.columns.year])
    print(stmt1)
    stmt1 = stmt1.where(empl.columns.name == own.columns.name)
    print(stmt1)

    updat = update(empl).values(number=stmt1)
    print(updat)

    results1 = conn.execute(stmt1).fetchall()
    conn.execute(updat)


    print(pd.DataFrame(results1))


    # updat = update(empl).values



# postgresql 에서 fetchall 이 안먹히네... 뭔가 다른게 있나 찾아봐야할듯함..





