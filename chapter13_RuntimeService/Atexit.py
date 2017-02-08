import atexit

# 인터프리터 종료 시점에 실행될 함수 등록하는 모듈임

def final_print(x):
    print(x)

atexit.register(final_print, 'Interpret finished')