# 비동기 네트워킹 프로그램 구현을 위한 모듈

# 비동기 HTTP 서버 예시
import asynchat, asyncore, socket
import os
import mimetypes

try:
    from http.client import responses            # 파이썬3
except ImportError:
    from httplib import response                 # 파이썬2


# asyncore  모듈에 결합되어 단순히 연결을 받는 역할
class async_http(asyncore.dispatcher):
    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockout(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        self.bind('', port)