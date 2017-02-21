import sqlite3

conn = sqlite3.connect("mydb")
cur = conn.cursor()
cur.execute("create table stocks (symbol text, shares integer, price real)")
conn.commit()

# 단일 데이터 입력
cur.execute("insert into stocks VALUES (?,?,?)", ('IBM', 50, 91.10))
cur.execute("insert into stocks VALUES (?,?,?)", ('AAPL', 150, 123.45))
conn.commit()

# 표의 값 집어넣는 반복 수행시
stocks =[('GOOG', 75, 380.13),
         ('AA', 60, 14.20),
         ('AIG', 125, 0.99)]
cur.executemany("insert into stocks VALUES (?,?,?)", stocks)

df = cur.execute("select * from stocks")
print(df.fetchall())
