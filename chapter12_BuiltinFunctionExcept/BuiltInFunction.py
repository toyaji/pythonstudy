# 임포트 필요없는 내장 함수들

# 절대값
print(abs(-10))

# 모두 true 인지
print(all([True, False, True]))

# 하나라도 true 인지
print(any([True, False, True]))

# 아스키문자로 출력 - 아스키 아닌 경우 '적절한 탈출 순서열' 로 변환됨. 밑에처럼...
print(ascii('ㅁ'))

# 이진 표현 문자열 반환
print(bin(482))

# 인자값 평가 true or false 반환, int 에서 상속 받은 함수라서 0, 1 숫자대신 사용 가능. 인자값 없으면 false
print(bool(15 > 10))
print(bool())

# 바이트 배열 형성(0~255사이), 작용방식은 정부배열과 거의 같아, 문자열 연산 사용시 'b' 값 붙여줘야함
l = [10, 100, 48, 254]
t = bytearray(b'abc\n\b')
a = bytearray(l)
print(a[2])
print(t.find(b'c'))

# 바이트 타입
print(bytes('a', encoding='UTF-8'))

# 정수값 받아서 문자 하나로 변환, 유니코드 범위 넘어가면 ValueError
print(chr(97))

# exec(), eval() 에서 사용할 수 있도록 문자열을 코드객체로 변환
# 첫번째 인자 string, 두번째 filename, 세번째 exec, eval, single flag 중에서... 이건 책 보삼...
a = compile('print("This is string command!")', '', 'single')
exec(a)

# 복소수 생성
print(complex(10, 38))

# 사전 타입 생성
a = dict(foo=3, bar=7)
print(a)

# 속성 이름 목록 반환
print(dir(a))

# 몫과 나머지를 튜플로 반환
print("%d, %d" % (divmod(20, 3)))

# iter 의 반복자 생성 - enumerate 객체 for 문 해야 인텍스, 키 값 볼수 있음
c = enumerate(l)
print(type(c))
for i in c:
    print(i)

# 표현식을 평가함, 보통 globals , locals 에 사전 넘겨줌
eval("print(p)", {'p' : [4, 9, 10]})

# 파이썬 문장 실행. 표현식과 문자열 차이는 ... ? http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python
# eval() 은 리턴값 주고, 대신 네임스페이스에 값 할당 못함. exec()는 가능함
exec("print(l)")

# 반복가능한 객체에서 첫번째 인자값의 함수에 조건 맞는 아이들만 true 넣어서 역시나 iter 객체 반환
# 데이터 걸러낼 목적이면 생성기나 코루틴이 빠름
print(filter(chr, ['a', 10, 'paul', 39.30]))

# 전역 네임스페이스 반환
print(globals())

# 해당 오브젝트의 속성 값인지 확인. 기면 true
# print(hasattr(c, str))

# 해시값
# print(hash(t))

# 이터 객체로 만들어줌 - 역시나 생성자가 더 빠름
a = iter(l)
for i in a:
    print(i)

# 첫번째 인자값인 function 에 두번째 인자값 대입해서 결과 값 리스트로 반환 - 그러나 생성기 표현식이 속도 더 좋음
a = map(hex, l)
b = [hex(x) for x in l]
print(a.__next__())   # 파이썬 3에서는 반복자로 생성이됨
print(b)

# 순서열역순 반환
a = reversed(l)
for i in a:
    print(i)

# 반올림
print(round(12.0345, 2))

# 정렬 - iterable 받아서 정렬값 반환하고, key= 값으로 비교함수 전달가능, reverse 넣으면 역순 정렬
l2 = [[2, 3], [4, 28], [3, 14], [20, 100]]
def get_second(list):
    return list[1]
r = sorted(l2, key=get_second, reverse=True)
print(r)

# __dict__ 를 반환함. 왜 있냐? __dict__ 에 직접 쓰는거 막야야되는  객체 때문에, 특별한 args 없는 경우 locals() 와 같음
print(vars(object))

# 주어진 변수 합쳐서 튜플 iter 로 만들어줌
z = zip('abc', [1,2,3], ['x', 'y'])
x = [x for x in z]
print(x)