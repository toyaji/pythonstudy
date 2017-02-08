# 순환 의존성 때문에 반납되지 못한 객체 찾는 모듈임
# 파이썬은 초기에 못잡은 순환 객체를 잡기 위해 세단계로 단계별 수집을 실시함

import gc

gc.collect()   # 쓰레기 모으는 함수, 인자값으로 0 ~ -2 주면 수집할 세대 나타내줌

gc.disable()   # 수집 비활성화

gc.enable()    # 수집 활성화

l = gc.garbage
# 더이상 사용 안되지만 순환참조 묶여있고
# __del__() 메서드 정의 있어서 쓰레기 수집 되지 못한 사용자 정의 인스턴스들을 담은 리스트
print(l)

print(gc.get_objects())   # 수집기에 의해서 추적되고 있는 모든 객체 표시

print(gc.get_referents(l))