class Naming:
    name = ['paul', 'kang']

    def __getattr__(self, i):
        return self.name[i]

        # 속성(Attribute)에 접근하려하는데 없는 경우에 던져주는 메서드
        # 얘만 정의했는데, 'AttributeError' 만 날려버리네.... 모지
        # 'This method should return the (computed) attribute value or raise an AttributeError exception.'
        # 이케 써있는데... 무슨 의미 인지 모르겠음...

    def __setattr__(self, key, value):
        self.name = value

        # Attribute 를 거꾸로 설정해 줄 수 있는 메서드


s = Naming

# print(s.super)

# 이거 지금 안먹히는데... 왜그러지?

# 일부로 잘못된 속성 접근 시도하는 경우

s.familyname = 'shin'

print(s.familyname)
