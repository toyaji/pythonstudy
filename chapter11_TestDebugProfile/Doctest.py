import doctest

from chapter11_TestDebugProfile import DocString

# doctest 라는 모듈있어서 여기서 모듈에 대한 테스트를 진행할 수 있음
nfail, ntests = doctest.testmod(DocString, verbose=True)   # 뒤에 verbose 옵션 주면 상세테스트 내용 보여줌. 없어도 무관

print([nfail, ntests])


# 별개 문서에 테스트 하지 않고 해당 모듈에서 자체로 하는 방법은 아래와 같음

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 테스트를 진행하는 방법은 문서화 문자열에 정의된 방법데로 나오는지를 보는 거임
# 그렇기 때문에 문서화 문자열에  >>> 로 꼭 상세 넣고 수정할때 docstring 도 수정해 놓아야함
