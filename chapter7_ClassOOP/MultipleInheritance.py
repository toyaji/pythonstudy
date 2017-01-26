from chapter7_ClassOOP.Inheritance import Evilaccount2

class DepositCharge(object):
    fee = 5.00
    def deposit_fee(self):
        self.withdraw(self.fee)

class WithdrawCharge(object):
    fee = 2.50
    def withdraw_fee(self):
        self.withdraw(self.fee)

# 위에 클래스 2개에서는 현재 withdraw 쓸 수 없지만 밑에서 다중 상속하고 나면 사용가능해짐
# 요런 클래스를 혼합클래스(mixin class) 라고 함


# java 랑 다르게 다중상속 제공하고 아래처럼 사용할 수 있음

class MostEvilAccount(Evilaccount2, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee()
        super().deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee()
        super().withdraw(amt)

d = MostEvilAccount("Paul", 500.00, 1.10)
# d.deposit_fee()
# d.withdraw_fee()

# 요렇게 실행하면 재귀 에러뜸. 왜냐면 현재 두 메소드 같은 경우 안에서 사용중인 메소드가 내부에서 정의되어 있지않고
# 상속받은 클래스에서 다중상속으로 정의를 해주기 때문에 문제가 됨.
# 여기서 생각할 수 있는게, 상속을 받은 클래스는 그 기반 클래스에 대한 순서를 속성값으로 가지고 있고
# 이 순서를 타고 올라가면서 속성을 찾아간다는 것임

print(MostEvilAccount.__mro__)

# 이 순서 값 보여주는게 바로 __mro__
