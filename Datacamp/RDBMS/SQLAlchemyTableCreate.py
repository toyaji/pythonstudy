from sqlalchemy import Table, Column, String, Integer, Float, Boolean, MetaData, create_engine

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/db1')

meta = MetaData()

data = Table('data', meta,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

meta.create_all(engine)

print(repr(meta.tables['data']))
