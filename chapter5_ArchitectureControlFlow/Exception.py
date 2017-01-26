try:
    raise TypeError
except (IOError, TypeError, NameError) as e:   # 이렇게 여러 에러 하나로 묶을 수도 있음
    print("Error Occur")

error_log = open(r'c:\Users\user\Desktop\error.txt', 'w')

try:
    raise IOError
except Exception as e:
    error_log.write('An error occurred : %s\n' % e)
    error_log.close()

# 에러 여러개 묶거나 구분없이 하나거나 위에 처럼 에러 기록할 필요있음
# 이렇게 에러를 기록하는 장치 없으면 디버깅 하기가 어려움

try:
    f = open(r'c:\Users\user\Desktop\error.txt', 'r')
except IOError as e:
    error_log.write('Unable to open : %s\n' % e)
else:
    data = f.readline()
    print(data)
finally:
    f.close()

# try 문에 else 넣게 되면 try 블록에서 에러가 발생하지 않은 경우에 실행됨
# finally 는 무조건 실행됨

KeyboardInterrupt
# Ctir + C 로 중단 명령 들어올때 일어나는 예외

NotImplementedError
# 구현안된 기능

RuntimeError
# 다목적용 범용 에러



# 에러는 계층화 되어 있어서 상위 에러로 잡으면 하위 에러들을 묶어서 다 잡아옴