import pdb

# pdb 모듈을 임포트 하면 파이썬 셸에서 디버깅이 가능함

pdb.run("print('Wow, its amazing')")
# 문자열 statement 수행 디버깅 ('continue' 입력하면 수행함)

pdb.runeval("print('Wow, its amazing')")
# 문자열  expression 수행 디버깅. 아래는 statement 와 expression 차이
print('http://hashcode.co.kr/questions/1402/statement%EC%99%80-expression%EC%9D%98-%EC%B0%A8%EC%9D%B4%EB%8A%94-%EB%AD%94%EA%B0%80%EC%9A%94')

pdb.runcall(str)
# 콜러블 함수를 호출함 디버깅안에


pdb.set_trace()  # 코드 중간에 집어넣어서 여기서부터 디버거가 시작하도록 할 수 있음(?)

