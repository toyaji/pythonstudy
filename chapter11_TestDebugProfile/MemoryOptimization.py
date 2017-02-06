import sys

print(sys.getsizeof(1))
print(sys.getsizeof("Hello World"))
print(sys.getsizeof([1, 2, 3, 4]))

# 시스 모듈에 getsizerof() 함수 사용하면 해당값이 얼마나 메모리 차지하고 있는 지 볼 수 있음
# 보여주는 숫자 단위는 바이트 단위