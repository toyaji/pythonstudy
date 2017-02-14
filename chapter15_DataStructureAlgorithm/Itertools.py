# 반복자 생성 관련 함수
from itertools import *

l = [1, 2, 3, 4, 5, 6, 7 ,7, 3, 4, 1, 3]
l1 = ['a', 'b', 'c']
l2 = 'paul'

# 여러 이터를 묶는 그룹형성하고 하나 다 토하면 다음 토하는 식으로 돌아감
c = chain(l, l1, l2)
for i in c:
    print(i, end="")

print()
# 위에랑 같은 생성자 만듬  - lists of list 처럼 iter 안에 iter 인 경우 생성자로 전환해줌
lil = ['paul', 'cume', 'chik', 'fork']
h = chain.from_iterable(lil)
for i in h:
    print(i, end="")

print()
# 길이가 r 인 순서열로 재조합 - 튜플로반환
r = combinations(lil, 2)
for i in r:
    print(i, end="")

print()
# n 부터 시작하는 연속된 정수 생성자 만들어줌
n = count(1000)
print(next(n))
print(next(n))

# iter 를 계속 순환하는 생성자
cy = cycle(l1)
t = 0
while t < 100:
    print(next(cy), end="")
    t += 1

print()
# 시작, 끝, 보폭 줘서 iter 만드는 방법
isl = islice(l, 2, 7, 2)
print(next(isl))
print(next(isl))

# 길이 r 인 모든 순열 반들어서 튜플로 반환. 앞에서 잘라서
p = permutations(l, 2)
for i in p:
    print(i, end='')

print()
# 데카르트 곱(cartesian product) 로 생성자 만들어줌
d = product(l1, l2)
for i in d:
    print(i, end='')

print()
# 하나의 오브젝트를 계속 만드는 생성자
o = repeat('Repeated Infinitely!!')
print(next(o))
print(next(o))

# 함수를 뱉어내는 생성자 만들 수 있음
def poob(x):
    return x*20

sp = starmap(poob, l1)
print(next(sp))
print(next(sp))
print(next(sp))

# predicate (= 람다가 좋은 예임) 가 true 인 동안 뱉어주는 녀석  - false 되면 바로 에러 보냄
tw = takewhile(lambda x: x < 5, l)
print(next(tw))

# predicate 가 false 인거만 반환  - 해당되는 놈만 보냄
ff = filterfalse(lambda x: x < 5, l)
print(next(ff))
print(next(ff))

# predicate 가 true 인 동안 iter 항목을 버려버림
dw = dropwhile(lambda x: x < 5, l)
print(next(dw))
print(next(dw))

# 똑같은 이터를 독립적으로 n 개 만들어냄 - 각각 돌아가는거임
a, b = tee(lil, 2)
print(next(a))
print(next(b))