# 전부 기재하지 않고 몇가지 특이한거만 정리해보자면...

EOFError

# 요거는 파일 끝났을대 나오는 에러인데, input() 으로 발생함
# read() 계열의 경우는 이 에러 안보내고 빈문자열 반환함


MemoryError

# 회복가능 메모리 부족


NotImplementedError

# 파생 클래스에서 필요한 메서드 구현이 안된 경우


OverflowError

# 정수값 너무 커서 표현 못할때


RuntimeError

# 특별한 범주에 들지 않을때... 젤 곤란하겠구나...


SystemError

# 인터프리터 내부에서 발생하는 에러, 문제 설명하는 문자열 제공

