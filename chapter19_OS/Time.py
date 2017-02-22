from datetime import time

# 시간객체 생성
t = time(14, 26, 59)
print(t)

# 시간대 설정 시 시간 대 뱉어냄
print(t.dst())

# 포맷형식
print(t.strftime('%I %p %M %S'))

