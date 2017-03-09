import os
from http.client import HTTPConnection

BOUNDARY = "$Python-Essential-Reference$"
CRLF = r'\r\n'

def upload(addr, url, formfields, filefields):
    # 폼 필드를 위한 구역 생성
    formsections = []
    for name in formfields:
        section = ['--' + BOUNDARY,
                   'Content-disposition: from-data; name="%s"' % name,
                   '', formfields[name]]
        formsections.append(CRLF.join(section) + CRLF)

    # 업로드할 모든 파일에 대한 정보 모음
    fileinfo = [(os.path.getsize(filename), formname, filename) for formname, filename, in filefields.items()]

    # 각 파일에 대해 HTTP 헤더 생성
    filebyte = 0
    fileheader = []
    for filesize, formname, filename in fileinfo:
        headers = ['--' + BOUNDARY,
                   'Content-disposition: from-data; name="%s"; filename="%s"' % name,
                   '', formfields[name]]
        fileheader.append(CRLF.join(headers) + CRLF)
        filebyte += filesize

    # 닫음 표시
    closing = "--" + BOUNDARY + r"--\r\n"

    # 전체 요청 길이 알아내기
    content_size = (sum(len(f) for f in formsections) +
                    sum(len(f) for f in fileheader) +
                    filebyte + len(closing))

    # 업로드
    conn = HTTPConnection(*addr)
    conn.putrequest("POST", url)
    conn.putheader("Content-type",
                   'multipart/form-date; boundary=%s' % BOUNDARY)
    conn.putheader("Content-lenth", str(content_size))
    conn.endheaders()

    # 모든 폼 구역을 보냄
    for s in formsections:
        conn.send(s.encode('utf-8'))

    # 모든 파일을 보냄
    if __name__ == '__main__':
        for head, filename in zip(fileheader, filefields.values()):
            conn.send(head.encode('utf-8'))
            f = open(filename, 'rb')
            while True:
                chunk = f.read(16384)
                if not chunk: break
                conn.send(chunk)
            f.close()

    # 파일을 몇개 올려봄..
server = ('localhost', 8080)
url = '/cgi-bin/upload.py'
formfields = {
    'name': 'Dave',
    'email': 'dave@daveaz.com'
}
filefields = {
    'file_1': '123.jpg',
    'file_2': '234.jpg'
}
resp = upload(server, url, formfields, filefields)
print(resp)