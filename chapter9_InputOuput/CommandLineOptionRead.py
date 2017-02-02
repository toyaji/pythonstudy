import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage : python %s inputfile outpufile\n" % sys.argv[0])
    raise SystemExit(1)
inputfile = sys.argv[1]
outputfile = sys.argv[2]

# 파이썬 실행하면 commandline 옵션들이 sys.argv 에 리스트로 저장됨. 이중 첫번째 값이 실행된 프로그램 네임

# 커맨드 옵션은 명령 실행시 주는 옵션인데 이거를 sys.argv 로 받아서 파이썬은 처리함
# Java에 String args[] 와 같은 기능임


