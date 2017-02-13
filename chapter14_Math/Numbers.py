# 다양한 숫자 종류 조직화 하기 위한 추상기반 클래스 정의해줌... (?)

import numbers

# 실제 객체 만들려고 쓰는 모듈 아니고 타입 검사를 위한 모듈임
# 상속받아서 만들려면 추가 안정성 검사 다 통과하도록 만들어야함

if isinstance(10+15j, numbers.Complex):
    print("It's a complex")
