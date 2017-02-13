import sys

sys._clear_type_cache()   # 내부 타입 캐시를 비움

# 파이썬은 최근에 사용된 메서드를 캐시로 모아둠. 상속관계등에서 속도 높이려고 ... 이걸 비워주는거임

print(sys._current_frames())   # 호출시점 가장 상위 스택프레임과 스레드 식별자(?) 를 매핑 반환함


try:
    raise RuntimeError
except RuntimeError as re:
    print(sys.exc_info())      # 현재 처리중인 예외 관한 정보 튜플로 반환, (클래스, 밸류, 트레이스백)

# sys.exit()  # 파이썬 종료시킴

print(sys.getdefaultencoding())  # 디폴트 인코딩 정보

print(sys.getfilesystemencoding())
# 내부 운영체제에서 사용되는 명칭으로 유니코드 파일 이름을 매핑하는데 사용되는 인코딩 반환함

print(sys._getframe())

print(sys.getrecursionlimit())  # 함수의 재귀 한도

print(sys.getrefcount(RuntimeError))  # 오브젝트의 참조 횟수

print(sys.getsizeof(list))  # 오브젝트의 바이트 크기 반환함. 문제는 __sizeof__ 로 정의된 값 그저 보여주는 거라서 내장타입 외에는 정확하지 않을 수 있다는 사실

print(sys.getwindowsversion())

# 윈도우스 버전 넘버 - https://msdn.microsoft.com/ko-kr/library/windows/desktop/ms724832.aspx
# 빌드 앤 서비스백 - https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions

sys.setswitchinterval(0.015)
print(sys.getswitchinterval())  # 현재 설정된 인터프리터의 스레드 스위치 주기

# 스레드 스위치 시간 설정한다고 해서 정확하게 돌아가는거 아님. 그리고 한 주기 끝난 다음에 어떤 스레드 실행할지는
# OS 에서 결정하기 때문에 파이썬이 그 자체로 스레드 스케쥴을 갖고 있거나 관리하는건 아님


