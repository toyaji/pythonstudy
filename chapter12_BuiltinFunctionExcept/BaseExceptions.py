# 가장 최상위 파파 에러 클래스
raise BaseException

# SystemExit, GeneratorExist, KeyboardInterrupt 예외를 제외한 모든 내장 예외 해당.
# 사용자 정의 예외 만들시 상속해야함
raise Exception

# 산술 예외 전부
raise ArithmeticError

# 색인 키 에러 전부
raise LookupError

# IO OS  등 파이썬 외부 발생 에러 포함
raise EnvironmentError