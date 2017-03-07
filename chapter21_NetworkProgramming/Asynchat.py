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
        # self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        client, addr = self.accept()
        return async_http_handler(client)

# 비동기 http 요청을 처리하는 클래스
class async_http_handler(asynchat.async_chat):
    def __init__(self, conn=None):
        asynchat.async_chat.__init__(self, conn)
        self.data = []
        self.got_header = False
        self.set_terminator(b'\r\n\r\n')

    # 들어오는 데이터를 받아서 데이터 버퍼에 추가
    def collect_incoming_data(self, data):
        if not self.got_header:
            self.data.append(data)

    # 종료기를 받았다
    def found_terminator(self):
        self.got_header = True
        header_data = b"".join(self.data)
        # 나중 처리를 위해서 헤더 데이터를 텍스트로 디코딩
        header_text = header_data.decode('utf-8')
        header_lines = header_text.splitlines()
        reqquest = header_lines[0].split()
        op = reqquest[0]
        url = reqquest[1][1:]
        self.process_request(op, url)

    # 텍스트를 나가는 스트림에 밀어넣음
    def push_text(self, text):
        self.push(text.encode('utf-8'))

    # 요청을 처리함
    def process_request(self, op, url):
        if op == "GET":
            if not os.path.exists(url):
                self.send_error(404, "File %s not found\r\n")
            else:
                type, encoding = mimetypes.guess_type(url)
                size = os.path.getsize(url)
                self.push_text("HTTP/1.0 200 OK\r\n")
                self.push_text("Content-length: %s\t\n" % size)
                self.push_text("Content-type: %s\t\n" % type)
                self.push_text("\r\n")
                self.push_with_producer(file_producer(url))
                self.send_error(501, "%s method not implemented" % op)
            self.close_when_done()

    # 에러처리
    def send_error(self, code, message):
        self.push_text("HTTP/1.0 %s %s\r\n" % (code, response[code]))
        self.push_text("Content-type: text/plain\r\n")
        self.push_text("\r\n")
        self.push_text("message")

class file_producer(object):
    def __init__(self, filename, buffer_size=512):
        self.f = open(filename, 'rb')
        self.buffer_size = buffer_size

    def more(self):
        data = self.f.read(self.buffer_size)
        if not data:
            self.f.close()
        return data

a = async_http(8080)
asyncore.loop()
