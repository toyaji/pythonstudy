import optparse
# 인터프리터 옵션을 디테일하게 설정하고 조정할 수 있는 모듈임

p = optparse.OptionParser()

# 인수 받아들이는 옵션 ( 옵션 자체를 새로 설정하는 실행부분임 )
p.add_option("-o", action="store", dest="outfile")     # store 하면 데스티네이션에다가 명령옵션 뒤에 오는 인자값 저장함
p.add_option("--output", action="store", dest="outfile")

# 불리언 플래그를 설정하는 옵션
p.add_option("-d", action="store_true", dest="debug")  # 데스티네이션에다가 불린값을 저장함
p.add_option("--debug", action="store_true", dest="debug")

# action 주면 해당 옵션값 들어왔을대 작동할 방법 설정하는 거임,

# 옵션의 기본 값을 설정
p.set_defaults(debug=False)     # 디폴트 옵션 설정하면 전체 옵션에 적용되는 거임. 모든 옵션에 다 일일이 적어줄 필요없게 하려고 하는거임

# 명령줄을 파싱
opts, args = p.parse_args()

# 옵션 설정값을 추출
outfile = opts.outfile
debugmode = opts.debug

print(outfile)
print(debugmode)
print(args)