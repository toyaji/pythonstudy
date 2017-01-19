import  sys

a = 37

b = sys.getrefcount(a)   # 시스템 상에서 해당 참조 사용 횟수 구하는 메서드

print(b)
