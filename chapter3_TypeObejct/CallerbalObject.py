class DistanceFrom(object):
    def __init__(self, origin):
        self.origin = origin

    def __call__(self, x):
        return abs(x - self.origin)

nums = [1, 37, 42, 101, 13, 9, -20]
nums.sort(key=DistanceFrom(10))
print(nums)

# callerble 을 설정하는 경우에 인스턴스 생성없이 바로 함수처럼 호출해서 사용이 가능함
# 위에 예시처럼 소팅하는 키 값에 바로 return 값을 줄 수가 있음


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

# __dir__ 정의하는 이유는 dir() 실행했을때 보여주고 싶지 않은거 숨기는 정도 용도?