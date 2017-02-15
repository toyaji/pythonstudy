from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)       # 소켓생성
s.bind(('', 8888))                     # 포트 8888에 묶음
s.listen(5)                            # 듣기 시작. 연결 제한을 5개로

while True:
    client, addr = s.accept()          # 연결을 받음
    print("Got a connection from %s" % str(addr))
    timestr = time.ctime(time.time()) + '\r\n'
    client.send(timestr.encode('ascii'))
    client.close()



