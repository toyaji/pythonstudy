# 타입과 관련 고성능 구현, 컨테이너 위한 추상클래스 설정 등 관련 모듈

import collections

# 아무쪽 끝이나 삽입 삭제가 가능한 큐 - 양쪽 끝 연산인 O(1) 빅오1로 똑같음...
dq = collections.deque(maxlen=10)   # 맥스렌 옵션 주면 범위 넘어서면 반대쪽끝 자동삭제하는 버퍼형태가 됨

# 오른쪽, 왼쪽 삽입
dq.append(10)
dq.appendleft(5)
print(dq)

# 비우기
dq.clear()

# iter 객체 통째로 넣기
iter = [x*2 for x in range(100)]
dq.extend(iter)
print(dq)

# 하나 뺌
print(dq.pop())
print(dq.popleft())

# 해당 값 제거
dq.remove(184)

# 모든 항목을 오른쪽으로 n 칸 옮김
dq.rotate(3)
print(dq)

#