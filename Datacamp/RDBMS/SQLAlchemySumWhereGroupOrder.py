from sqlalchemy import create_engine, Table, MetaData, select, func, or_, and_

engine = create_engine(r'sqlite:///C:\Users\paul\Downloads\Chinook_Sqlite.sqlite')

meta = MetaData()

with engine.connect() as con:
    print(engine.table_names())
    play = Table('Playlist', meta, autoload=True, autoload_with=engine)      # 테이블 객체 먼저 만들어서 sqlalchemy 이용하기
    album = Table('Album', meta, autoload=True, autoload_with=engine)
    genre = Table('Genre', meta, autoload=True, autoload_with=engine)
    customer = Table('Customer', meta, autoload=True, autoload_with=engine)

    print('\n', play.columns)     # 칼럼명 조회하려면 요렇게 명령 주면 됨
    print(album.columns)
    print(genre.columns)
    print(customer.columns)

    stmt = select([play.columns.Name, album.columns.Title])                        #  테이블 두개에서 데이터 같이 끌어오는 명령임
    stmt1 = select([play.columns.Name, func.sum(album.columns.AlbumId)])           #  func 라는 모듈에 보면 sum 주는 방법 있음
    stmt2 = select([play.columns.Name, func.sum(album.columns.AlbumId).label('Alsum')])           #  func 라는 모듈에 보면 sum 주는 방법 있음

    stmt = stmt.where(or_(play.columns.Name == 'Movies', play.columns.Name == 'Classical'))   # 특정조건 맞는 애들만 가져오는 방법인데, 그중에도 or_ and_ 함수가 sqlalchemy에 있음
    stmt1 = stmt1.order_by(play.columns.PlaylistId)                                           # 특정 열 기준으로 순서 맞춰서 보여줌
    stmt2 = stmt2.group_by(play.columns.Name)                                                 # 위에 끌어온 테이블을 특정 컬럼을 중심으로 그루핑 하는 명령


    print('\n', stmt)
    print(stmt1)
    print(stmt2)

    results = con.execute(stmt).first()        # 첫번째만 가져오는 방법임
    results1 = con.execute(stmt1)
    results2 = con.execute(stmt2).fetchall()   # fetchall 안하면 resultproxy 객체로 끌어옴   .scalar() 로 끌어오면 바로 객체 타입을 str 로 가져옴

    print('\n', type(results2), '\n')     # fetchall 하면 리스트 객체로 가져오고

    for r in results:
        print(r)

    for r in results1:
        print(r)

    print(results2[0].keys())            # 위에서 라벨 붙여서 칼럼에 이름 준 상태라서 리스트 맨 첫줄에 해당 라벨명 나옴

    for r in results2:
        print(r)

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(results2)
df.columns = results2[0].keys()          # 판다 데이터 프레임으로 결과 넣고 여기다가 다시 키값을 컬럼 명으로 설정하는 방법

print(df.head())

df.plot.bar()                            # 멧플롯에서 바차트로 만들어주는 방법임
plt.show()
