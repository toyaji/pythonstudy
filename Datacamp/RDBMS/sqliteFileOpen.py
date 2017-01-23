from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(r'sqlite:///C:\Users\user\Downloads\Chinook_Sqlite.sqlite')
# 다운받은 데이터 가져와서 엔진만들어줌

con = engine.connect()
# 연결을 해야지만 쓸수 있어

rs = con.execute("SELECT name FROM sqlite_master WHERE type='table'")
# 현재 데이터에서 테이블명 가져오는 명령문

rs1 = con.execute('SELECT * FROM Album ')
# 'Album 열의 전체 가져오는 명령문


df = pd.DataFrame(rs.fetchall())

df1 = pd.DataFrame(rs1.fetchall())
# 판다 데이터 프레임으로 해당 열 가져오기

con.close()

print(df)

print(df1.shape)
print(df1.head())

