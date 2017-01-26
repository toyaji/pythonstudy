class Upperstr(str):
    def __new__(cls, value=''):
        return str.__new__(cls, value.upper())

u = Upperstr("hello")

print(u)

#  __new__ 는 클래스가 생성되는 시점에 정의되는 거임. 다시 말하면, 인스턴스가 생기기 전에 클래스에 먼가를 넣을 수 있는거임

# 인스턴스가 일단 생성되면, 참조 횟수 세기(reference counting) 을 통해 관리되며, 참조 횟수가 0이 되면 즉시 파괴됨.
# 요때 클래스안에 __del__ 이 있나 보고 있으면 요거부터 호출함
# 우리가 주의해야하는 점은 del 명령이 __del__ 과 같은건 아니야, del 은 참조횟수를 없애는거고 __del__ 은 참조횟수가 없어지면 실행되는 거뿐

# 이러다보니까 __del__ 을 잘못 재정의하게 되면 순환참조 쓰레기 수집기 등에 의해서 객체가 알아서 처리되지 않을 위험이 있음


class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.observers = set()

    def __del__(self):
        for ob in self.observers:
            ob.close()
        del self.observers

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def withdraw(self, amt):
        self.balance -= amt
        self.notify()


class AccountObserver(object):
    def __init__(self, theaccount):
        self.theaccount = theaccount
        theaccount.register(self)

    def __del__(self):
        self.theaccount.unregister(self)
        del self.theaccount                  # theaccount 객체만 삭제할 뿐 해당 객체가 참조하고 있던 녀석들을 삭제하지 않게됨. 그거는 위쪽클래스에 정의되어 있으니까

    def update(self):
        print("Balace is %0.2f" % self.theaccount.balance)

    def close(self):
        print("Account no longer in use")

a = Account('Dave', 1000.00)
a_ob = AccountObserver(a)

# 위에 예시는 순환참조되는 경우로, 하나를 삭제해도 참조가 남아서 쓰레기 수집기가 작동하지 않음. 이에 따라 메모리 영구누수가 발생함
# 이렇게 되면 시스템 꺼야지만 메모리 복구 되기 때문에 장기간 실행하는 프로그램에서는 상당히 위험함



# 이런 문제 해결하는 방법이 바로 약한참조(weak reference) 인데, 객체에 대한 참조숫자를 늘리지 않고 참조를 생성함... 신기방기


import weakref       # 약한 참조 생성을 위해 사용하는 모듈

class AccountObserver(object):
    def __init__(self, theaccount):
        self.accountref = weakref.ref(theaccount)    # 요 부분이 약한 참조 생성하는 방법임 !!!
        theaccount.register(self)
