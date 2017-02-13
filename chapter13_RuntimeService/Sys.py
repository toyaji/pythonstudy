import sys

# 인터프리터 작동 및 환경 관련 함수&변수

print(sys.api_version)   # 인터프리터의 C API 버전 표시 - 확장 모듈 다룰 때 사용

print(sys.builtin_module_names)  # 파이썬 자체 실행파일에 내장된 모듈명 튜플로 보여줌

print(sys.byteorder)  # 기계의 고유한 바이트순서 - 리틀 엔디안 or 빅 엔디안 (https://firejune.com/1790/%EB%B9%85%EC%97%94%EB%94%94%EC%95%88%EA%B3%BC+%EB%A6%AC%ED%8B%80%EC%97%94%EB%94%94%EC%95%88+%EA%B0%9C%EB%85%90)

print(sys.dont_write_bytecode)  # 모듈 임포트시 바이트코드(.pyc, .pyo 파일) 쓸지 여부 결정하는 불리언

print(sys.exec_prefix)  # 플랫폼 종속적인 파일 설치될 디렉터리 (말이 좀 어렵네...)

print(sys.flags.debug)  # 인터프리터 옵션 정보 나타내는 속성들 가지고 있음. 불리언 플래그

print(sys.maxsize, 2**31-1) # 32비트인데 현재는, 최대 정수 길이

print(sys.maxunicode)  # 현재 인코딩에서 표현가능한 최대 유니코드 포인트

print(sys.platform)

print(sys.version)

print(sys.version_info)  # 버전 정보를 튜플로 보여줌 (major, minor, micro, releaselevel, serial)

# 파이썬 3.5 면  메이저 3, 마이너 5  ... 이 뒤로는... releaselevel 은 alpha, beta, candidate, final 로 4단계

print(sys.winver)  # 윈도우에서 레지스트리 키를 만드는데 사용되는 버전 번호


