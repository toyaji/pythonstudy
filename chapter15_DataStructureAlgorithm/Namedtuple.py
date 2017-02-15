from collections import namedtuple

# 튜플 색인으로만 검색해야하는 한계 때문에 큰 튜플에서 검색이 어려움. 따라서 필드마다 이름붙여서 이름으로 검색하게 해주는거임
# 앞에 타입명, 뒤에 필드명(속성 이름 목록)
NetworkAddress = namedtuple('NetworkAddress', ['hostname', 'port'])
a = NetworkAddress('www.python.org', 80)

print(a.hostname)

# 해당 namedtuple 은 일반 튜플의 하위 클래스임
print(isinstance(a, tuple))

