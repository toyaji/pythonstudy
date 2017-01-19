# 일반 참조

a = [1, 2, 3, 4]
b = a

print(a is b)

# shallow copy : 리스트나 컨테이너 복사에 적용되고,
# 새로운 리스트 만들지만, 구성요소는 참조만 가져와서 공유됨.

a = [1, 2, [3, 4]]
b = list(a)
print(a is b)

b.append(10)
print(a, b)

a[2][1] = -100

print(a, b)

# deep copy : 재귀적 복사로 구성요소도 공유하지 않음.

import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

a[2][1] = -100

print(a, b)