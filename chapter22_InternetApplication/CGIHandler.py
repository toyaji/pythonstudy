# 간편 핸들러를 이용한 CGI (Common gateway interface) 스크립트 실행하는 웹 서버

from http.server import HTTPServer, CGIHTTPRequestHandler
import os

# 문서 루트 디렉터리로 이동
os.chdir("/home/httpd/html")
# CGIHTTP 서버를 8080 포트에서 시작
serv = HTTPServer(("", 8080), CGIHTTPRequestHandler)
serv.serve_forever()
