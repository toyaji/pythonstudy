# object.__bool__(self)
# 객체 자체의 bool 값을 설정해 주는 거임. 만약에 설정안하면 __len__() 이 호출되고
# 두 가지 다 설정 없으면 그냥 'true' 로 던져줌

class test(object):
    def __init__(self):
        self.a = 10
        self.b = 10

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.a == self.a and other.b == self.b
        # 어떤 식으로 서로 비교해서 bool 값 돌려줄지 적어주는거임. 이걸로 비교연산자 사용가능해짐

    def __hash__(self):
        return hash((self.a, self.b))

        # __eq__ 가 일단 정의되어 있어야지 효율적으로 쓸 수 있음(?)

t = test()
p = test()

print(test.__bool__(t))
print(t == p)   # 비교가능해짐

#  __hash__ 의  용도는 솔직히 잘 모르겠음... ㅠㅠ


print(hash(t))

