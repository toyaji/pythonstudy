s = set([1, 5, 10, 15, 'a'])
f = frozenset(['a', 37, 'hello', 10])

s1 = set([1, 10])
f1 = frozenset([45, 'b'])


print(s.difference(f))
print(s.intersection(f))
print(s.isdisjoint(f1))  # 교집합 전혀 없는 경우에 True 반환
print(s1.issubset(s))  # 부분집합 확인
print(s.issuperset(s1)) # 포함집합 여부 확인
print(s.symmetric_difference(f))  # 교집합을 제외한 합집함 : 대칭 차집합 반환

s.difference_update(f) # 차집합만 남겨줌
print(s)

s.intersection_update(s1) # r교집합만 남겨줌
print(s)