import random
from chapter7_ClassOOP.Class import Account
# 같은 패키기 안에 정의해놓은 클래스를 일단 가져와야함

class Evilaccount(Account):
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 4.10
        else:
            return self.balance

# 상속받아서 함수 재정의하는 경우

c = Evilaccount("George", 1000.00)
c.deposit(10.0)
print(c.inquiry() )


class Evilaccount2(Account):
    def __init__(self, name, balance, evilfactor):
        Account.__init__(self, name, balance)        # init 새로 재정의 하면서 기존 상속받은 클래스의 내용 가져오려면 해야함
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 4.10
        else:
            return self.balance


class MoreEvilAccount(Evilaccount):
    def deposit(self, amt):
        self.withdraw(5)
        super().deposit(amt)

# 파이썬 3 에서는 super() 로 overridden  된 함수 호출하는 데 유용하게 쓸 수 있음
