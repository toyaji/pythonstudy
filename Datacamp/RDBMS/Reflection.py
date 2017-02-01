from sqlalchemy import Table, create_engine, MetaData

# 엔진 연결부
engine = create_engine(r'sqlite:///C:\Users\user\Downloads\Chinook_Sqlite.sqlite')


# Table 클래스 쓰려면 먼저 메타데이터 있어야 하는데... 메타데이터란? 데이터를 위한 데이터로 도서관의 카드목록표와 같은 경우임
metadataexplain = 'https://ko.wikipedia.org/wiki/%EB%A9%94%ED%83%80%EB%8D%B0%EC%9D%B4%ED%84%B0'
print("메타데이터에 대한 위키백과 설명 : %s" % metadataexplain)

meta = MetaData()
    

# Table 클래스를 이용해서 이미 있는 데이터베이스 안의 스키마 객체에 맞게 정보 끌어옴(?) 이 과정을 reflection 이라고 함
tb = Table('Employee', meta, autoload=True, autoload_with=engine)

print()
print(repr(tb), '\n')
print(tb.columns.keys(), '\n')
print(repr(meta.tables['Employee']))   # 위 쪽에 테이블 repr 값과 메타데이터가 반영하고 있는 값이 같은 상태임