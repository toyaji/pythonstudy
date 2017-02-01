import tweepy, math, urllib, sys

print(sys.modules)    # 현재 파일에 사용된 모든 모듈 보여주는 딕셔너리


from chapter8_ModulePackage.ImportEx import a, foo

a = 42
foo()          # a 를 재정의하더라도 임포트 한 함수에서 사용하는 전역변수는 해당 임포트한 문서에서 끌어다 쓰는거임!
print(a)
