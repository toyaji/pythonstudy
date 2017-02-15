from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))          # 서버에 연결
tm = s.recv(1024)                       # 1024 바이트가지만 받음
s.close()
print("The time is %s" % tm.decode('ascii'))


