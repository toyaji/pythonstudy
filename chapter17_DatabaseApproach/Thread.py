# 해당 db 모듈이 다중스레드 안전을 보장하는지 알 수 있음

import psycopg2 as pg
import pymysql as pm

"""
0 : 스레드안전보장 x -> 여러스레드가 모듈 공유하면 안됨
1 : 안전 보장 -> 그래도 연결 공유하면 안됨
2 : 모듈 및 연결 안전 보장 -> 커서 공유 안됨
3 : 모듈, 연결, 커서 모두 안전 보장
"""
print(pg.threadsafety)
print(pm.threadsafety)
