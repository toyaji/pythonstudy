class Stock(object):
    __slots__ = ['name', 'shares', 'price']
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# 요런식으로 슬롯 이용해서 들어오는 인스턴스 제한하면 메모리 적게 먹고 시간효율 현저히 향상됨
# 문제는 슬롯 설정하면  __dict__ 속성이 안먹혀서 여기 엵어있는 애들이 작동 안하는 수가 있음

