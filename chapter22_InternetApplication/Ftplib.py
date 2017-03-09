# FTP 프로토콜에서 클라이언트 쪽 구현하는 모듈임 (File Transfer Protocol)
# HTTP 보다 빠르게 파일 보낼 수 있고 안정선 획득할 수 있음 -> 서버 구축해서 대용량 파일 공유하는데 유용함

import ftplib

# FTP 연결을 위한 객체 생성
f = ftplib.FTP('ftp.kaist.ac.kr')

# 익명 사용자로 접속하기
f.login(user='anonymous', passwd='guest')

# 현재 작업 폴더 디렉터리 목록 생성
dir = f.dir()

print()
# 현재 작업 path 변경
f.cwd('vim')
dir2 = f.dir()

# 특정 폴더에다가 폴더 내려받기
with open(r'C:\Users\user\Downloads\vim.html', 'wb') as file:
    f.retrbinary("RETR faq.html", file.write)

# 현재 패스에 폴더 만들기 - 여기는 거부됨
# f.mkd('paul')
f.close()