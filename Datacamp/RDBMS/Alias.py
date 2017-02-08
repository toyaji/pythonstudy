from sqlalchemy import *
import pandas as pd

engine = create_engine(r"sqlite:///C:\Users\Paul\Downloads\Chinook_Sqlite.sqlite")

meta = MetaData()
print(engine.table_names())

with engine.connect() as con:
    employees = Table('Employee', meta)
    customers = Table('Customer', meta)
    print(employees.primary_key)
    print(customers.key)


# sqlalchemy 로 테이블 만들어서 쓰는 방식 너무 불편함 그냥 판다스로 쿼리 날리는게... 백배 낳은듯...
# alias() 는 두 테이블간의 참조 만드는 메서드임