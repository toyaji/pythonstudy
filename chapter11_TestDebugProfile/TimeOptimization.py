import time

# time 모듈에서 해당 함수로 cpu 소요시간 하고 실제 소요시간 측정할 수 있음
start_cpu = time.clock()
start_real = time.time()

# 타임측정을 위한 실험용 명령
list = []

with open('c:\\Users\\user\\PycharmProjects\\kospi.csv', 'r') as f:
    for line in f:
        list.append(line.split(','))
print(list)


end_cpu = time.clock()
end_real = time.time()

print("%f Real Seconds" % (end_real - start_real))
print("%f CPU Seconds" % (end_cpu - start_cpu))


# 더 짧은 시간 단위 벤치마크 측정하고 싶다면 아래 모듈 사용하면 됨
from timeit import timeit, repeat

a = timeit('math.sqrt(2.0)', 'import math')
# 첫번째 인수는 벤치마크 하려는 코드, 두번째 인수는 실행환경 설정용 명령으로 한번만 실행 -> 보여주는 시간은 백만번 실행한 시간
print(a)

b = repeat('sqrt(2.0)', 'from math import sqrt')
# repeat 함수는 세번 실행하고 리스트로 보여줌. 여기서 중요한거는 임포트를 어떻게 하느냐가 속도에 엄청난 차이를 가져온다는점
print(b)