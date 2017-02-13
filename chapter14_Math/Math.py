# math 모듈은 정수와 실수에 대해서만 작동하고, 복소수 계산하고 싶으면 cmath 모듈  써야함
import math

# 내장 상수
print(math.pi)
print(math.e)

# 무한대 생성 및 확인
inf = float("-inf")
print(math.isinf(inf))
na = float("nan")
print(math.isnan(na))

# 0에 가까운 쪽으로 정수 자르는 함수
print(math.trunc(15.1923))

# 정수와 소수로 나눠서 튜플 반환
print(math.modf(math.pi))

# 나머지 반환 - 플로트로 반환
print(math.fmod(15, 4))

