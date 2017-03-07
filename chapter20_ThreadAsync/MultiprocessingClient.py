# 클라리언트 예시

from multiprocessing.connection import Client
import hashlib

auth = hashlib.sha512()
conn = Client(('localhost', 15000), authkey=auth.update(b'12345'))

conn.send((3, 4))
r = conn.recv()
print(r)

conn.send(("Hello", " World"))
r = conn.recv()

print(r)
conn.close()