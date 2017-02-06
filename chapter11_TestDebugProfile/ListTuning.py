from timeit import timeit

# 리스트와 collections.deque() 의 수행시간 비교
# 리스트의 경우 맨 앞에다가 넣을려면 뒤에 있는 애들 다 밀어내는 구조로 짜여있음. 그러다보니 계산 많이 할수록 시간 급격히 늘어
# 반면에 deque 의 경우 앞으로 붙이는 경우에 속도 차이 현저히 빠름

a = timeit('s.appendleft(37)', 'import collections; s = collections.deque()', number=1000000)
b = timeit('s.insert(0, 37)', 's=[]', number=1000000)

print(a, b)