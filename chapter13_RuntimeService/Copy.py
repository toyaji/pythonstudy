import copy

a = [10, 20, 30, 40]

# 얕은 복사 하는 함수, 문제는 실제로 쓸일 거의 없음
# 클래스 내에서 __copy__ 설정할 때만 주로 쓰임
# 이거 이상하네...
c = copy.copy(a)
print(a is c)

d = copy.deepcopy(a)
print(a is d)
