# 경고 메시지 출력하고 걸래내는 기능 제공
import warnings, os


# 경고 메시지 필터링 가능 ( 인터프리터에 -W 옵션 줘서 할 수도 있음)
# action : error 경고를 에러로 , ignore 무시, always 항상 출력, default 경고 발생위치서 한번, module 발생 모듈서 한번, once 무조건 한번
warnings.filterwarnings(action='ignore', message=".*might.*", category=DeprecationWarning)

# 경고는 출력하고 에러처럼 프로그램 멈춰 버리지 않는 것이 특징. 그러나 쉽게 에러로 변형할 수도 있음
warnings.warn("feature X is deprecated.")
warnings.warn("feature Y might be broken.", RuntimeWarning)
warnings.warn("it might be ignored", DeprecationWarning)

fpath = os.path.realpath(__file__)  # 현재 파일경로 가져오는 방법

with open('c:\\users\\user\\downloads\\traceback.txt', 'a') as f:
    # 파일에다가 경고 메시지 쓰는 방법
    warnings.showwarning("this go into file", UserWarning, fpath, 16, f)


warnings.resetwarnings()   # 경고 필터 초기화