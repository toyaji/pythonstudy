nums = [1, 2, 3 ,4, 5]
square = [n * n for n in nums]

# 리스트 내포 문법의 예시


a = [-3, 5, 2, -10, 7, 8]
b = 'abc'

e = [(x, y) for x in a for y in b if x > 0]

print(square)
print(e)

import math

f = [(1, 2), (3, 4), (5, 6)]
g = [math.sqrt(y*x + y*y) for x, y in f]   # 주의할 점은 튜플값은 반드시 괄호로 묶어줘야함

# sqrt() 루트값 리턴하는 함수

print(g)