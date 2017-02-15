# 힙으로 우선순위 큐를 구현
# 힙 자료 구조 설명 : http://blog.eairship.kr/249

import heapq

l = [1, 304, 29, 293, 85, 39, 55, 78, 120, 345, 276, 199]

# 리스트를 제자리에서 힙으로 변환시킴
heapq.heapify(l)
print(l)

# 가장 작은 위에 녀석 팝시킴
print(heapq.heappop(l))

# 힙 유지하면서 하나 추가
heapq.heappush(l, 16)
print(l)

# 하나 추가하고 가장작은놈 하나 빼옴  - push _> pop 순서임 : 젤 작은놈 빼로 바로 나옴
heapq.heappushpop(l, 170)
print(l)

# 먼저 제거하고 하나 집어넣음
heapq.heapreplace(l, 3)
print(l)

# iterable 중에서 가장 큰 n 개로 구성된 리스트 뽑아냄 - 순서는 큰놈부터
print(heapq.nlargest(3, l))

# 반대로 작은놈 뽑아냄
print(heapq.nsmallest(3, l))