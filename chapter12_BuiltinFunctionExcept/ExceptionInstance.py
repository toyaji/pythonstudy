try:
    raise EnvironmentError("Error message in args!", 'Seconds args')
except EnvironmentError as ee:
    print(ee.args)

# 예외 발생실 전달한 인수들이 args 라는 인스턴스에 들어감

# 기타는 부록에서 계속... 잘 안쓰는 내용인듯?

