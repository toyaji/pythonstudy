# 유니코드 문자에 대한 속성 담은 유니코드 문자 데이터베이스 접근하는 모듈
import unicodedata

# 해당 유니코드 글자에 할당된 양방향 범주 정보 반환
print(unicodedata.bidirectional('@'))

# 해당 유니코드의 일반 범주 반환
print(unicodedata.category('☆'))

# 이름으로 유니코드 문자 검색
print(unicodedata.lookup('COPYRIGHT SIGN'))
print(unicodedata.lookup('BAMUM LETTER PHASE-A UNKNOWN'))
print('http://www.unicode.org/charts')

# 유니코드 데이터버전 반환
print(unicodedata.unidata_version)