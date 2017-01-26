# __dict__ 속성으로 인스터스의 고유 데이터를 딕셔너리로 볼 수 있음

from chapter7_ClassOOP.ObjectMemoryManagement import Account

a = Account('Guido', 1100.0)

a.number = 12345   # 인스턴스에 변화주거나 __dict__ 에 직접 변화줘도 인스턴스에 영향미침
print(a.__dict__)
print(a.__class__)   # 클래스에 연결된거 볼수있음

print(Account.__dict__.keys())   # 클래스의 사전에 가면 메소드가 다 들어있음

