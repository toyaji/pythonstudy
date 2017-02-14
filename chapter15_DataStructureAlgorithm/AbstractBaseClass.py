"""
컬렉션 모듈에는 추상기반 클래스 담아져 있는데,
1. 내장 컨테이너 흉내낸 사용자 정의 클래스 만드는 경우
2. 타입검사를 위해서 사용함
"""
from collections import *

Container  # 최상위

Hashable

Iterable

Iterator   # iterable 상속받고 next() 정의됨

Sized      # 크기 알수 있는 컨테이너를 위한 기반 클래스

Callable

Sequence   # Container, iterable, sized 상속

MutableSequence   # 변경가능한 순서열을 위한 기반 클래스, sequence 상속받고 setitem, delitem, append, pop, remove 같은거 제공

Set        # Container, iterable, sized 상속, 집합 연산 관련 함수들 들어있음

MutableSet # set 상속받고 add, discard 정의됨

Mapping

MutableMapping

MappingView



