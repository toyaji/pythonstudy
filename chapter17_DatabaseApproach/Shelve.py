# 전에 오브젝트 파일로 넣는거 할때 한번 다뤘던 모듈인데,
# 선반 객체를 사용한 객체 지속성 지원하는 모듈

import shelve

# 해시테이블 기반 데이터 베이스 사용해서 디스크 저장되는거 배고 딕셔너리랑 같음

# 객체 생성
s = shelve.open('shelvedb', 'c')

s['first'] = [str, float, dict]
print(s.keys())

s.close()