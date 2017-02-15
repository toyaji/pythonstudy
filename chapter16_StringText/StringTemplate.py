# 문자열 치환을 간단히 할 수 있는 새로운 문자열 타입 template 정의 모듈

from string import Template, capwords
import string

t = Template("This is whole new object")

ma = {'T' : 'WoW', 'n': 'P'}
# 매핑 오브젝트를 받아서 템플릿 객체의 스트링에 치환함   -  정확히 어떻게 작동하는지...
t.substitute(ma)
print(t.template)

# 대문자로 첫글짜만
print(capwords('psualsjeljh'))
