import optparse

# 유닉스 스타일 명령줄 옵션 처리하는 모듈

# 옵션 파서 객체 생성
p = optparse.OptionParser()

# 새로운 옵션 추가 - 인수는 옵션 이름으로 만들어 줄거...
# 인수 없는 단순 옵션
p.add_option("-t", action="store_true", dest='tracing')

# 문자열 인수 받는 옵션
p.add_option('-o', '--outfile', action="store", type='string', dest='outfile')

# 정수 인수 받는 옵션
p.add_option('-d', '--debug', action="store", type='int', dest='debug')


# 이밖에도 많이 있음.. 그러나 명령줄 옵션 건드릴 일이 얼마나 있을까...