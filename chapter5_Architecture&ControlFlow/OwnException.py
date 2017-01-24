import sys
class NetworkError(Exception): pass

# 새로 예외 만들려면 클래스로 생성하고 Exception 을 상속하면됨


class DeviceError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

print(TypeError.args)

try:
    raise DeviceError(1, "Not Responding")
except:
    print(sys.exc_info())
    a = sys.exc_info()[2]

# .args 설정하면 역추적 메시지 출력할 때 사용된다는데... 잘 모르겠음..;



# raise TypeError.with_traceback(a)

# BaseException object 가 뭔지 잘 모르겠음..ㅠ
