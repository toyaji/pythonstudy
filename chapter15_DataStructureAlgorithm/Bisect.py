# 리스트 정렬하고 순서 관리 하는 모듈
import bisect

l = [1, 2, 3, 4, 6, 7]

# 리스트에서 정렬된 순서를 유지하기 위해서 item 을 어디에 넣으면 되는지 색인을 반환함
c = bisect.bisect(l, 5)
print(c)

# 어느쪽에서부터 순서따져 들어갈지
right = bisect.bisect_left(l, 5)
left = bisect.bisect_right(l, 5)
print(right, left)

# 정렬 순서에 맞춰 집어넣음
bisect.insort(l, 5)
print(l)

