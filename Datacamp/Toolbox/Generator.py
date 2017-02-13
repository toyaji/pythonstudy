# 제너레이터 의 경우엔 다른게 만드는 순간이 아니라 쓰는 순간에 메모리쓴다는게 큰 차이
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

lengths = (len(person) for person in lannister)
print(type(lengths))
print(next(lengths))


# 제너레이터 함수 만들기
def get_lenght(input_list):
    for person in input_list:
        yield len(person)

c = get_lenght(lannister)
print(next(c))
for p in c:
    print(p)

