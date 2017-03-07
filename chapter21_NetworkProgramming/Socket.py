import socket

# 광범위하게 쓰이는 함수로 주소에 대한 정보를 리스트로 가져옴
addr = socket.getaddrinfo("www.rebalance.co.kr", 80)
print(addr)

# 이름으로 호스트명 가져옴
host = socket.gethostbyname("www.rebalance.co.kr")
print(host)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 80))

# 지역머신 호스트 이름 ?
print(socket.gethostname())

# 인터넷 서비스 이름과 해당 서비스의 포트번호 반환
t = socket.getservbyname('https', 'tcp')
print(t)

