# 원거리에 있는 컴퓨터에 프로세스 할당하는 서버, 클라이언드 생성가능함

# 서버 예시
from multiprocessing.connection import Listener
import hashlib

auth = hashlib.sha512()
serv = Listener(('', 15000), authkey=auth.update(b'12345'))
while True:
    conn = serv.accept()
    while True:
        try:
            x, y = conn.recv()
        except EOFError:
            break
        result = x + y
        conn.send(result)
    conn.close()
