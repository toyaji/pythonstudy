# 현재 인터프리터 옵션에 -i, -v 준 상태임

import warnings

# 경고 내보내는 내장 모듈 가지고 있음. 모듈 임포트 하지 않더라도 인터프리터에 -w 에 옵션 넣어줘도됨
# 아래 예시는 경고 만드는 예
warnings.warn("You should re-check weather this item is possible", UserWarning)

# 발생 시킬 수 있는 warning 종류 - 다양함...

raise DeprecationWarning('사용이 권장되지 않는 기능')
raise SyntaxError('사용이 권장되는 않는 파이썬 문법')


# 경고는 어떻게 발생시키냐 따라서 프로그램을 멈추게 할수도 있고 계속 진행되게 할 수도 있음
