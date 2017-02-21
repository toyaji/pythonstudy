# 파일 이름 매칭 관련 모듈

import fnmatch

from re import findall

print(fnmatch.fnmatch('foo.git', '*.git'))
print(fnmatch.fnmatch('part37.html', 'part3[0-5].html'))

