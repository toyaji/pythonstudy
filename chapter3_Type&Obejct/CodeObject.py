
code_object = compile('print("Hello World")', '<paul>', 'single')

# 컴파일이라는 function 으로 CodeObject 생성할 수 있음.
# 싱글은 한 줄만 실행시킬 수 있음, 여러줄 넣게 되면 에러남

print(code_object)
exec(code_object)  # codeobject 실행시킬 때는 요런식으로...


codeA = """print("Hello World")
print("How are you?")"""

code_object = compile(codeA, '<Hello>', 'exec')

# exec 로 입력하면 여러줄 실행이 가능함
exec(code_object)

# code_object = compile(codeA, '<Hello>', 'eval')
# exec(code_object)
# eval 로 입력하면 TraceBack 해서 어디 틀렸는지 보여주는 용도(?), 한줄식만 실행함


print(dir(code_object))
print(code_object.co_stacksize)
print(code_object.co_filename)
print(code_object.co_firstlineno)