class Account(object):    # 특별한 상속할 클래스 없으면 최상위 클래스인 object 상속시키면 됨
    num_account = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


# self 는 java의 this와 같음. 없으면 지역변수로 인식함