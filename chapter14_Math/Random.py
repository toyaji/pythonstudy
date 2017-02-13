# 유사 무작위 생성과 관련한 함수
import random

# 생성기의 시트 뿌려는데.. none 이면 기본적으로 현재 시간에서 가져옴
random.seed()

# 난수 생성기의 현재 상태 반환
print(random.getstate())

# k 개의 무작위 비트 담은 긴 정수 생성
print(random.getrandbits(10))

# 범위 내의 난수 생성
print(random.randint(1, 100))

# 범위 내에서 스텝까지 설정가능한 함수
print(random.randrange(0, 100, 10))

# 순서열을 무작위로 만들어줌
l = [1, 2, 3, 4, 5]
print(random.choice(l))       # 한개 뽑아
print(random.sample(l, 3))    # 몇개 담은 리스트 반환
random.shuffle(l)
print(l)                      # 순서 섞어버림

# 무작위 실수 분포 관련함수
print(random.random())        # 0.0 ~ 1.0 사이에서 반환
print(random.uniform(1, 10))  # a ~ b 사이의 균일분포 무작위 수 반환

# 모듈내에 내장하고 있는 기타 랜덤 생성기 - os 의 랜덤 생성기 가져다가 쓰는 방법임
wil = random.SystemRandom()
print(wil.random())