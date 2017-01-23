from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(r'sqlite:///C:\Users\user\Downloads\Chinook_Sqlite.sqlite')

# 작업 끝나면 자연스럽게 커넥트 끊기도록 하는 방법임

with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")  # from 열에서 선택한 행 가져오는 명령문
    rs1 = con.execute('SELECT * FROM Employee WHERE EmployeeId >=6')
    df = pd.DataFrame(rs.fetchmany(size=4))   # fatchall 하면 너무 많아서 필요한거만 가져올때 사이즈정해줌
    df1 = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()   # 키값 가져와서 칼럼명 채워주는 방법임



print(df)
print(df1)