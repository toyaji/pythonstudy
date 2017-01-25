import math
x = 4
a = eval('3*math.sin(3.5+x) + 7.2')
print(a)

# eval() 은 표현식 담은 문자열 실행하고 결과값 돌려줌



a = [3, 5, 10, 13]
exec("for i in a: print(i)")
# 파이썬 코드를 담은 문자열을 실행함


globals = {'x' : 7, 'y': 10, 'birds' : ['Parrot', 'Swallow', 'Albatross']}
locals = {}

# eval 이나 exec 는 전역네임스페이스나 로컬 네임스페이스 받아서 쓸 수 있음

a = eval("3 * x + 4 * y", globals, locals)
exec("for b in birds: print(b)", globals, locals)



# compile 함수는 문자열을 바이트 코드로 컴파일함.
# 마지막 인자값인 kind 는 single 은 단일문장, exec 는 여러문장, eval 은 표현식


s = "for i in range(0,10): print(i)"
c = compile(s, '', 'exec')
exec(c)


s2 = "3*x + 4*y"
c2 = compile(s2, '', 'eval')
print(eval(c2))