from urllib.request import urlopen, HTTPError,URLError, Request

url =  'https://torrentkim5.net'      # 토렌트킴 사이트 인데 ssl 걸어놓고 기본적으로 403 블락도..
url1 = 'http://www.naver.com'
u = urlopen(url1)
data = u.read(100)
print(data)

# HTTP 응답코드 반환
print(u.getcode())

# 에러를 객체로 해서 관리하는법
try:
    uu = urlopen(url)
    print(uu.read())
except (HTTPError, URLError) as e:
    print(e)


# request 객체를 활용해서 브라우저를 이용해서 접속하는 것처럼 헤더 추가하기
from fake_useragent import UserAgent
ua = UserAgent()
header = {
    'User-Agent': ua.chrome
}
r = Request(url, headers=header)
u = urlopen(r)
print(u.read(100))

# 헤더 반환
print(r.get_header('User-Agent'))

# url 타입 반환
print(r.get_full_url())
print(r.type)