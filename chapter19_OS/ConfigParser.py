# 윈도우 ini 설정 파일 읽는데 사용 - ini 파일은 텍스트 파일로 프로그램 설정 파일의 표준형식임
# ini 파일 구조에 대해서는 https://ko.wikipedia.org/wiki/INI_%ED%8C%8C%EC%9D%BC

from configparser import ConfigParser

default = {'basedir': 'c:\\Users\\user\\Downloads'}

# 컨피그 파서 인스턴스 생성하고 읽어오기 - 디폴트 설정값을 먼저 사전으로 생성해놓고 쓸 수 있음
c = ConfigParser(default)
c.read('c:\\Users\\user\\Downloads\\my.ini')

# 디폴트 값 반환
print(c.defaults())

# 모든 구역 이름 반환
print(c.sections())

# 특정 구역의 옵션 값 가져오기
print(c.get('mysqld', 'port'))

# 옵션이 있는지 여부
print(c.has_option('client', 'port'))

# 섹션의 옵션들 가져옴
print(c.items('mysqld'))

# 섹션 더하기
c.add_section('paulset')

# 섹션에 아이템 더하기
c.set('paulset', 'test', '1234')

# 섹션 삭제
c.remove_section('myisamchk')
print(c.has_option('paulset', 'test'))


# 최종적으로 써야함.. ini 로..
f = open('c:\\Users\\user\\Downloads\\my2.ini', 'w')
c.write(f)