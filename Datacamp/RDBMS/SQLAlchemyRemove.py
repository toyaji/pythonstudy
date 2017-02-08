from sqlalchemy import create_engine, MetaData, Table, select, delete, or_
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:happygk2@localhost:5432/postgres')

meta = MetaData()

with engine.connect() as conn:

    own2 = Table('owner2', meta, autoload=True, autoload_with=engine)
    own1 = Table('owner1', meta, autoload=True, autoload_with=engine)

    stmt = delete(own2)
    print(stmt)
    conn.execute(stmt)

    # 조건 맞는 애들만 찾아서 지우는법
    stmt = delete(own1).where(
        or_(own1.columns.name == '신바울', own1.columns.year == 1)
    )

    print(stmt)
    conn.execute(stmt)

    # 테이블 없애버리는 명령
    own2.drop(engine)
    print(own2.exists(engine))

    # 테이블 다 지우는 방법
    # meta.drop_all(engine)