import socket

# 패킷 일방적으로 받아서 출력
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 10000))
while True:
    data, address = s.recvfrom(256)
    print("Received a connection from %s" % str(address))
    s.send(b"echo:" + data, address)

