import traceback, sys

# 예외 추적 관련 모듈

try:
    raise RuntimeError
finally:
    f = open('c:\\users\\user\\downloads\\traceback.txt', 'w')
    tb = sys.exc_info()[2]                                          # 트레이스백 객체 가져옴
    traceback.print_tb(tb, file=f)                                  # 트레이스백 항목을 파일로 내보내고, stderr 로 메시지 띄워줌
    f.close()

    print(traceback.format_exc())   # 위에 꺼랑 똑같은거를 출력으로 보여주는 거임
    print(traceback.extract_tb(tb)) # 역추적 정보가 담고 있는 정보 리스트로 반환함 ( 파일명, 라인, 펑션명, 텍스트)

"""
    try:
        raise ArithmeticError
    finally:
        f = open('c:\\users\\user\\downloads\\traceback.txt', 'a')
        tb = sys.exc_info()[2]  # 트레이스백 객체 가져옴
        print(sys.exc_info())
        traceback.print_exception(ArithmeticError, ArithmeticError.__cause__, tb, file=f)
        f.close()

        # 프린트 익셉션에서 value 가 뭔지 모르겠음.. ㅠㅠ
"""