import sqlite3

# 데이터 베이스는 메모리로 해서 실행하는 방법 - 프로그램 종료되면 날라감...
# timeout 은 락 얼마동안 할지, isolation level 은 락 종류 (기본은 deferred: 연산 실제 수행되기전에 롹 안걸어...)
# detect_types 는 결과값 반환시 추가로 타입검사함 - SQL 타입 말하는거임..
db = sqlite3.connect(":memory:", timeout=6, isolation_level='EXCLUSIVE')


# 명령문 온전하면 True 반환
s = 'select * from memory;'
b = sqlite3.complete_statement(s)
print(b)

# 사용자 정의 함수 만드는 방법
def toupper(s):
    return s.upper()

db.create_function("toupper", 1, toupper)         # 라벨이름, 넘겨줄 파라미터, 사용할 함수


# 사용자 정의 집계 함수 만드는 방법 - step 과 finalize 가 정의된 클래스가 반드시 필요함 ( 주어진 값으로 스텝을 반복적으로 실행)
class Averager(object):
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def step(self, value):
        self.total += value
        self.count += 1

    def finalize(self):
        return self.total / self.count

db.create_aggregate("myavg", 1, Averager)
# db.execute("select myavg(num) from sometable")

# 사용자 정의 대조 함수를 등록함 - 값 두개 받아서 비교하고 -1 , 0 , 1 로 반환하는 함수여야함
def name(x, y):
    if x > y: return 1
    elif x == y: return 0
    else: return -1

db.create_collation('compare', name)


# 현재 실행중인 질의 취소
db.interrupt()

# 복원용 덤프 만ㄷ르기
db.iterdump()

# n 번 명령 시행시마다 실행할 역호출 함수 등록
def shown():
    return "It occur 8times"
db.set_progress_handler(shown, 8)

db.close()