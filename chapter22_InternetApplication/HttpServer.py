# 기본 http 서버 구현

from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

class MyHTTPServer(ThreadingMixIn, HTTPServer):
    def __init__(self, addr, handler, subnet):
        HTTPServer.__init__(self, addr, handler)
        self.subnet = subnet

    def verify_request(self, request, client_address):
        host, port = client_address
        if not host.startwith(self.subnet):
            return False
        return HTTPServer.verify_request(self, request, client_address)

# 서버 실행
serv = MyHTTPServer(('', 8080), SimpleHTTPRequestHandler, '192.168.69.')
serv.serve_forever()