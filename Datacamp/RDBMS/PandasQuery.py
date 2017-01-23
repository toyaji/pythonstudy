from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(r"sqlite:///C:\Users\Paul\Downloads\Chinook_Sqlite.sqlite")
# 앞에 sqlite:/// 안빠지게 주의할것 !

df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId>=6 ORDER BY Birthdate', engine)
# 판다스 안에 내장되어 있는 기능으로 쿼리 쉽게 날릴 수 있음

print(df)

# 양쪽 테이블에다가 각각 칼럼 만들어 내는 명령문 INNER JOIN
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())