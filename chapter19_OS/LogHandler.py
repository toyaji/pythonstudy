from logging import handlers, FileHandler, StreamHandler

# UDP 서버에 로그 메시지 보냄 - 손실되는거 보장안함
import sys

handlers.DatagramHandler(host='localhost', port=80)

# 파일에다가 씀
f = FileHandler('./paulapp.log', encoding='utf-8')

# HTTP 서버에 업로드
handlers.HTTPHandler(host='localhost', url='www.naver.com')

# 메모리에 수집하다가 일정 수준되면 타켓 핸들러로 보내버림
handlers.MemoryHandler(1000, target=f)

# 로그 파일이 일정 수준 넘어가면 새로 파일 따옴
handlers.RotatingFileHandler('./paulapp.log', maxBytes=10000)

# 이리 열린 파일객체에다가 내보냄
StreamHandler(sys.stderr)